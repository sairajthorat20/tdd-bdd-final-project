# Copyright 2016, 2024 John Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test cases for Account Model

Test cases can be run with:
    nosetests
    coverage report -m
"""

import os
import logging
from unittest import TestCase
from datetime import date
from service import app
from service.models import Account, DataValidationError, db
from tests.factories import AccountFactory

DATABASE_URI = os.getenv(
    "DATABASE_URI", "sqlite:///test.db"
)


######################################################################
#  A C C O U N T   M O D E L   T E S T   C A S E S
######################################################################
class TestAccountModel(TestCase):
    """Test Cases for Account Model"""

    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        Account.init_db(app)

    @classmethod
    def tearDownClass(cls):
        """This runs once after the entire test suite"""
        db.session.close()

    def setUp(self):
        """This runs before each test"""
        db.session.query(Account).delete()  # clean up the last tests
        db.session.commit()

    def tearDown(self):
        """This runs after each test"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_an_account(self):
        """It should Create an Account and assert that it exists"""
        fake_account = AccountFactory()
        account = Account(
            name=fake_account.name,
            email=fake_account.email,
            address=fake_account.address,
            phone_number=fake_account.phone_number,
            date_joined=fake_account.date_joined,
        )
        self.assertIsNotNone(account)
        self.assertEqual(account.id, None)
        account.create()
        self.assertIsNotNone(account.id)
        self.assertEqual(account.name, fake_account.name)
        self.assertEqual(account.email, fake_account.email)
        self.assertEqual(account.address, fake_account.address)
        self.assertEqual(account.phone_number, fake_account.phone_number)
        self.assertEqual(account.date_joined, fake_account.date_joined)

    def test_read_an_account(self):
        """It should Read an Account"""
        account = AccountFactory()
        account.create()
        found_account = Account.find(account.id)
        self.assertIsNotNone(found_account)
        self.assertEqual(found_account.id, account.id)
        self.assertEqual(found_account.name, account.name)
        self.assertEqual(found_account.email, account.email)
        self.assertEqual(found_account.address, account.address)
        self.assertEqual(found_account.phone_number, account.phone_number)
        self.assertEqual(found_account.date_joined, account.date_joined)

    def test_update_an_account(self):
        """It should Update an Account"""
        account = AccountFactory()
        account.create()
        self.assertIsNotNone(account.id)
        original_id = account.id

        account.name = "Updated Name"
        account.update()
        self.assertEqual(account.id, original_id)

        # Fetch it back and verify name change
        accounts = Account.all()
        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].id, original_id)
        self.assertEqual(accounts[0].name, "Updated Name")

    def test_update_without_id(self):
        """It should raise DataValidationError when updating without an id"""
        account = AccountFactory()
        account.id = None
        self.assertRaises(DataValidationError, account.update)

    def test_delete_an_account(self):
        """It should Delete an Account"""
        account = AccountFactory()
        account.create()
        self.assertEqual(len(Account.all()), 1)
        account.delete()
        self.assertEqual(len(Account.all()), 0)
        found_account = Account.find(account.id)
        self.assertIsNone(found_account)

    def test_list_all_accounts(self):
        """It should List all Accounts in the database"""
        accounts = Account.all()
        self.assertEqual(accounts, [])
        for _ in range(5):
            account = AccountFactory()
            account.create()
        accounts = Account.all()
        self.assertEqual(len(accounts), 5)

    def test_find_by_name(self):
        """It should Find an Account by Name"""
        accounts = AccountFactory.create_batch(3)
        for account in accounts:
            account.create()
        name = accounts[0].name
        count = len([account for account in accounts if account.name == name])
        found = Account.find_by_name(name)
        self.assertEqual(len(found), count)
        for account in found:
            self.assertEqual(account.name, name)

    def test_serialize_an_account(self):
        """It should serialize an Account"""
        account = AccountFactory()
        data = account.serialize()
        self.assertNotEqual(data, None)
        self.assertIn("id", data)
        self.assertEqual(data["id"], account.id)
        self.assertIn("name", data)
        self.assertEqual(data["name"], account.name)
        self.assertIn("email", data)
        self.assertEqual(data["email"], account.email)
        self.assertIn("address", data)
        self.assertEqual(data["address"], account.address)
        self.assertIn("phone_number", data)
        self.assertEqual(data["phone_number"], account.phone_number)
        self.assertIn("date_joined", data)
        self.assertEqual(data["date_joined"], account.date_joined.isoformat())

    def test_deserialize_an_account(self):
        """It should deserialize an Account"""
        data = AccountFactory().serialize()
        account = Account()
        account.deserialize(data)
        self.assertNotEqual(account, None)
        self.assertEqual(account.id, None)
        self.assertEqual(account.name, data["name"])
        self.assertEqual(account.email, data["email"])
        self.assertEqual(account.address, data["address"])
        self.assertEqual(account.phone_number, data["phone_number"])
        self.assertEqual(account.date_joined, date.fromisoformat(data["date_joined"]))

    def test_deserialize_without_date_joined(self):
        """It should deserialize an Account without date_joined using today's date"""
        data = AccountFactory().serialize()
        del data["date_joined"]
        account = Account()
        account.deserialize(data)
        self.assertEqual(account.date_joined, date.today())

    def test_deserialize_missing_data(self):
        """It should not deserialize an Account with missing data"""
        data = {"id": 1, "name": "Foo"}
        account = Account()
        self.assertRaises(DataValidationError, account.deserialize, data)

    def test_deserialize_bad_data(self):
        """It should not deserialize bad data"""
        data = "this is not a dictionary"
        account = Account()
        self.assertRaises(DataValidationError, account.deserialize, data)

    def test_repr(self):
        """It should represent an Account as a string"""
        account = AccountFactory()
        account.id = 1
        account.name = "Foo"
        self.assertEqual(repr(account), "<Account Foo id=[1]>")
