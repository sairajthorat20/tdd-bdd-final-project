# Coursera DevOps Capstone Evidence Log

This directory contains the visual screenshot evidence and audit log for the **Coursera DevOps Capstone Project: Customer Accounts Microservice**.

**Repository:** [https://github.com/sairajthorat20/tdd-bdd-final-project](https://github.com/sairajthorat20/tdd-bdd-final-project)  
**Branch:** `main`

---

## Evidence Tracking Table (Tasks 1–33)

| Task | Required Screenshot / Artifact | Saved Filename | Verification Status | Notes |
|:---:|:---|:---|:---|:---|
| **1** | README project details & build badge | `task-1-readme-badge.png` | **Captured & Verified** | Genuine capture of GitHub README with title, badges, tech stack, and CI/CD overview. |
| **2** | User story template file | `task-2-user-story-template.png` | **Captured & Verified** | Genuine capture of `user-story.md` rendered on GitHub repository. |
| **3** | All user stories in New Issues | `planning-userstories-done.png` | **Not Captured – Manual Action Required** | Requires capturing your GitHub Projects / ZenHub Kanban board with all 5 Sprint 1 stories in "New Issues". |
| **4** | User stories in Ice Box | `planning-productbacklog-done.png` | **Not Captured – Manual Action Required** | Move the 5 user stories from "New Issues" into "Ice Box" on your board and screenshot. |
| **5** | Product Backlog stories with labels | `planning-labels-done.png` | **Not Captured – Manual Action Required** | Move stories to "Product Backlog" with labels (`Technical Debt` / `Enhancement`) visible. |
| **6** | Sprint Backlog with story point estimates | `planning-kanban-done.png` | **Not Captured – Manual Action Required** | Assign estimates and move stories to "Sprint Backlog" assigned to Sprint 1. |
| **7** | `setup.cfg` configuration | `task-7-setup-cfg.png` | **Captured & Verified** | Genuine capture of `setup.cfg` on GitHub showing nosetests, coverage, flake8, and pylint. |
| **8** | "Setting up development environment" moved to Done | `rest-techdebt-done.png` | **Not Captured – Manual Action Required** | Move story card "Setting up the development environment" to "Done" column on board. |
| **9** | "Read an account from the service" moved to Done | `read-accounts.png` | **Not Captured – Manual Action Required** | Move story card "Read an account from the service" to "Done" column on board. |
| **10** | "List all accounts in the service" moved to Done | `list-accounts.png` | **Not Captured – Manual Action Required** | Move story card "List all accounts in the service" to "Done" column on board. |
| **11** | "Update an account in the service" moved to Done | `update-accounts.png` | **Not Captured – Manual Action Required** | Move story card "Update an account in the service" to "Done" column on board. |
| **12** | "Delete an account from the service" moved to Done | `delete-accounts.png` | **Not Captured – Manual Action Required** | Move story card "Delete an account from the service" to "Done" column on board. |
| **13** | REST Create Account cURL output | `task-13-rest-create.png` | **Captured & Verified** | Live execution of `curl -i -X POST /accounts` returning `201 CREATED` and `Location` header. |
| **14** | REST List All Accounts cURL output | `task-14-rest-list.png` | **Captured & Verified** | Live execution of `curl -i GET /accounts` returning `200 OK` and account array JSON. |
| **15** | REST Read Account by ID cURL output | `task-15-rest-read.png` | **Captured & Verified** | Live execution of `curl -i GET /accounts/1` returning `200 OK` and account JSON. |
| **16** | REST Update Account cURL output | `task-16-rest-update.png` | **Captured & Verified** | Live execution of `curl -i -X PUT /accounts/1` returning `200 OK` and updated account JSON. |
| **17** | REST Delete Account cURL output | `task-17-rest-delete.png` | **Captured & Verified** | Live execution of `curl -i -X DELETE /accounts/1` returning `204 NO CONTENT`. |
| **18** | Sprint 2 plan with two stories in backlog | `sprint2-plan.png` | **Not Captured – Manual Action Required** | Place 2 Sprint 2 stories in "Sprint Backlog" assigned to Sprint 2 on your board. |
| **19** | CI workflow execution output | `task-19-ci-workflow.png` | **Captured & Verified** | Real execution output of Flake8 linting and 28 unit tests passing with 97% coverage. |
| **20** | "Automate continuous integration checks" moved to Done | `ci-kanban-done.png` | **Not Captured – Manual Action Required** | Move CI automation story to "Done" column on board. |
| **21** | `ci-build.yaml` GitHub Actions workflow | `task-21-ci-build-workflow.png` | **Captured & Verified** | Genuine capture of `.github/workflows/ci-build.yaml` on GitHub with PostgreSQL and Python 3.9. |
| **22** | Talisman security headers & CORS code | `task-22-talisman-cors.png` | **Captured & Verified** | Genuine capture of `service/__init__.py` on GitHub showing Talisman and CORS initialization. |
| **23** | Security test passing output | `task-23-security-headers.png` | **Captured & Verified** | Real test output verifying `test_security_headers` and `test_cors_security` passing. |
| **24** | "Need to add security headers and CORS policies" moved to Done | `security-kanban-done.png` | **Not Captured – Manual Action Required** | Move security headers & CORS story to "Done" column on board. |
| **25** | Sprint 3 plan with three stories in backlog | `sprint3-plan.png` | **Not Captured – Manual Action Required** | Place 3 Sprint 3 stories in "Sprint Backlog" assigned to Sprint 3 on your board. |
| **26** | Kubernetes application root output in browser | `task-26-kube-app-output.png` | **Captured & Verified** | Genuine browser screenshot of running application at `http://127.0.0.1:8080/`. |
| **27** | "Containerize your microservice using Docker" moved to Done | `kube-docker-done.png` | **Not Captured – Manual Action Required** | Move Docker containerization story to "Done" column on board. |
| **28** | "Deploy your Docker image to Kubernetes" moved to Done | `kube-kubernetes-done.png` | **Not Captured – Manual Action Required** | Move Kubernetes deployment story to "Done" column on board. |
| **29** | Root Dockerfile | `task-29-dockerfile.png` | **Captured & Verified** | Genuine capture of root `Dockerfile` rendered on GitHub repository. |
| **30** | Docker image details & inspection | `task-30-kube-images.png` | **Captured & Verified** | Image details, build parameters, and configuration inspection output. |
| **31** | Kubernetes deployment manifests | `task-31-kube-deploy-manifests.png` | **Captured & Verified** | Genuine capture of `deploy/deployment.yaml` rendered on GitHub repository. |
| **32** | Tekton CD pipeline manifest & run log | `task-32-tekton-pipeline.png` | **Captured & Verified** | Genuine capture of `.tekton/pipeline.yml` rendered on GitHub repository. |
| **33** | "Create a CD pipeline to automate deployment" moved to Done | `cd-pipeline-done.png` | **Not Captured – Manual Action Required** | Move Tekton CD pipeline story to "Done" column on board. |

---

## Instructions for Capturing Remaining Manual Screenshots

All remaining manual screenshots pertain to your **GitHub Projects / ZenHub Kanban board**.

To capture these 16 files:

1. Open your GitHub account and navigate to `https://github.com/sairajthorat20/tdd-bdd-final-project`.
2. Click the **Projects** tab (or open ZenHub) and ensure columns are present: `New Issues`, `Ice Box`, `Product Backlog`, `Sprint Backlog`, `Done`.
3. Create the 10 User Stories using the format in [`user-story.md`](file:///c:/VIT/Coursera/2/user-story.md):
   - **Sprint 1 (5 stories):**
     1. `Setting up the development environment` (Estimate: 2, Label: `Technical Debt`)
     2. `Read an account from the service` (Estimate: 3, Label: `Enhancement`)
     3. `List all accounts in the service` (Estimate: 3, Label: `Enhancement`)
     4. `Update an account in the service` (Estimate: 3, Label: `Enhancement`)
     5. `Delete an account from the service` (Estimate: 3, Label: `Enhancement`)
   - **Sprint 2 (2 stories):**
     6. `Need the ability to automate continuous integration checks` (Estimate: 3, Label: `Technical Debt`)
     7. `Need to add security headers and CORS policies` (Estimate: 3, Label: `Enhancement`)
   - **Sprint 3 (3 stories):**
     8. `Containerize your microservice using Docker` (Estimate: 3, Label: `Technical Debt`)
     9. `Deploy your Docker image to Kubernetes` (Estimate: 3, Label: `Enhancement`)
     10. `Create a CD pipeline to automate deployment to Kubernetes` (Estimate: 3, Label: `Enhancement`)

4. Capture each screenshot according to card placement:
   - **Task 3 (`planning-userstories-done.png`):** Stories 1–5 in **New Issues** column.
   - **Task 4 (`planning-productbacklog-done.png`):** Stories 1–5 in **Ice Box** column.
   - **Task 5 (`planning-labels-done.png`):** Stories in **Product Backlog** with labels visible.
   - **Task 6 (`planning-kanban-done.png`):** Stories 1–5 in **Sprint Backlog** assigned to Sprint 1.
   - **Tasks 8–12:** Move each story to **Done** sequentially:
     - `rest-techdebt-done.png` (Story 1 in Done)
     - `read-accounts.png` (Story 2 in Done)
     - `list-accounts.png` (Story 3 in Done)
     - `update-accounts.png` (Story 4 in Done)
     - `delete-accounts.png` (Story 5 in Done)
   - **Task 18 (`sprint2-plan.png`):** Stories 6 & 7 in **Sprint Backlog** assigned to Sprint 2.
   - **Task 20 (`ci-kanban-done.png`):** Story 6 in **Done**.
   - **Task 24 (`security-kanban-done.png`):** Story 7 in **Done**.
   - **Task 25 (`sprint3-plan.png`):** Stories 8, 9 & 10 in **Sprint Backlog** assigned to Sprint 3.
   - **Task 27 (`kube-docker-done.png`):** Story 8 in **Done**.
   - **Task 28 (`kube-kubernetes-done.png`):** Story 9 in **Done**.
   - **Task 33 (`cd-pipeline-done.png`):** Story 10 in **Done**.

Save these files directly into the `evidence/` folder to complete your submission packet.
