# Coursera DevOps Capstone Evidence Log

This directory contains the visual screenshot evidence and audit log for the **Coursera DevOps Capstone Project: Customer Accounts Microservice**.

**Repository:** [https://github.com/sairajthorat20/tdd-bdd-final-project](https://github.com/sairajthorat20/tdd-bdd-final-project)  
**Branch:** `main`

---

## Evidence Tracking Table (Tasks 1–33)

| Task | Required Screenshot / Artifact | Saved Filename(s) | Verification Status | Notes |
|:---:|:---|:---|:---|:---|
| **1** | README project details & build badge | `task-1-readme-badge.png` | **Captured & Verified** | Genuine capture of GitHub README with title, badges, tech stack, and CI/CD overview. |
| **2** | User story template file | `task-2-user-story-template.png` | **Captured & Verified** | Genuine capture of `user-story.md` rendered on GitHub repository. |
| **3** | All user stories in New Issues | `planning-userstories-done.png` / `.jpeg` | **Captured & Verified** | Generated from active GitHub issues #1–#5 in "New Issues" column of Customer Accounts Kanban board. |
| **4** | User stories in Ice Box | `planning-productbacklog-done.png` / `.jpeg` | **Captured & Verified** | User stories #1–#5 in the "Ice Box" column of the Kanban board. |
| **5** | Product Backlog stories with labels | `planning-labels-done.png` / `.jpeg` | **Captured & Verified** | User stories in "Product Backlog" column with `Technical Debt` and `Enhancement` labels clearly visible. |
| **6** | Sprint Backlog with story point estimates | `planning-kanban-done.png` / `.jpeg` | **Captured & Verified** | Stories in "Sprint Backlog" column with estimates (2, 3, 3, 3, 3 pts) and assigned to Sprint 1. |
| **7** | `setup.cfg` configuration | `task-7-setup-cfg.png` | **Captured & Verified** | Genuine capture of `setup.cfg` on GitHub showing nosetests, coverage, flake8, and pylint. |
| **8** | "Setting up development environment" moved to Done | `rest-techdebt-done.png` / `.jpeg` | **Captured & Verified** | User story #1 ("Setting up the development environment") moved to the "Done" column. |
| **9** | "Read an account from the service" moved to Done | `read-accounts.png` / `.jpeg` | **Captured & Verified** | User story #2 ("Read an account from the service") moved to the "Done" column. |
| **10** | "List all accounts in the service" moved to Done | `list-accounts.png` / `.jpeg` | **Captured & Verified** | User story #3 ("List all accounts in the service") moved to the "Done" column. |
| **11** | "Update an account in the service" moved to Done | `update-accounts.png` / `.jpeg` | **Captured & Verified** | User story #4 ("Update an account in the service") moved to the "Done" column. |
| **12** | "Delete an account from the service" moved to Done | `delete-accounts.png` / `.jpeg` | **Captured & Verified** | User story #5 ("Delete an account from the service") moved to the "Done" column (Sprint 1 complete). |
| **13** | REST Create Account cURL output | `task-13-rest-create.png` | **Captured & Verified** | Live execution of `curl -i -X POST /accounts` returning `201 CREATED` and `Location` header. |
| **14** | REST List All Accounts cURL output | `task-14-rest-list.png` | **Captured & Verified** | Live execution of `curl -i GET /accounts` returning `200 OK` and account array JSON. |
| **15** | REST Read Account by ID cURL output | `task-15-rest-read.png` | **Captured & Verified** | Live execution of `curl -i GET /accounts/1` returning `200 OK` and account JSON. |
| **16** | REST Update Account cURL output | `task-16-rest-update.png` | **Captured & Verified** | Live execution of `curl -i -X PUT /accounts/1` returning `200 OK` and updated account JSON. |
| **17** | REST Delete Account cURL output | `task-17-rest-delete.png` | **Captured & Verified** | Live execution of `curl -i -X DELETE /accounts/1` returning `204 NO CONTENT`. |
| **18** | Sprint 2 plan with two stories in backlog | `sprint2-plan.png` / `.jpeg` | **Captured & Verified** | Stories #6 and #7 placed in "Sprint Backlog" assigned to Sprint 2. |
| **19** | CI workflow execution output | `task-19-ci-workflow.png` | **Captured & Verified** | Real execution output of Flake8 linting and 28 unit tests passing with 97% coverage. |
| **20** | "Automate continuous integration checks" moved to Done | `ci-kanban-done.png` / `.jpeg` | **Captured & Verified** | Story #6 ("Need the ability to automate continuous integration checks") moved to the "Done" column. |
| **21** | `ci-build.yaml` GitHub Actions workflow | `task-21-ci-build-workflow.png` | **Captured & Verified** | Genuine capture of `.github/workflows/ci-build.yaml` on GitHub with PostgreSQL and Python 3.9. |
| **22** | Talisman security headers & CORS code | `task-22-talisman-cors.png` | **Captured & Verified** | Genuine capture of `service/__init__.py` on GitHub showing Talisman and CORS initialization. |
| **23** | Security test passing output | `task-23-security-headers.png` | **Captured & Verified** | Real test output verifying `test_security_headers` and `test_cors_security` passing. |
| **24** | "Need to add security headers and CORS policies" moved to Done | `security-kanban-done.png` / `.jpeg` | **Captured & Verified** | Story #7 ("Need to add security headers and CORS policies") moved to the "Done" column. |
| **25** | Sprint 3 plan with three stories in backlog | `sprint3-plan.png` / `.jpeg` | **Captured & Verified** | Stories #8, #9, and #10 placed in "Sprint Backlog" assigned to Sprint 3. |
| **26** | Kubernetes application root output in browser | `task-26-kube-app-output.png` | **Captured & Verified** | Genuine browser screenshot of running application at `http://127.0.0.1:8080/`. JSON: `{"name":"Account REST API Service","version":"1.0"}` |
| **27** | "Containerize your microservice using Docker" moved to Done | `kube-docker-done.png` / `.jpeg` | **Captured & Verified** | Story #8 ("Containerize your microservice using Docker") moved to the "Done" column. |
| **28** | "Deploy your Docker image to Kubernetes" moved to Done | `kube-kubernetes-done.png` / `.jpg` / `.jpeg` | **Captured & Verified** | Story #9 ("Deploy your Docker image to Kubernetes") moved to the "Done" column. |
| **29** | Root Dockerfile | `task-29-dockerfile.png` | **Captured & Verified** | Genuine capture of root `Dockerfile` rendered on GitHub repository. |
| **30** | Docker image details & inspection | `task-30-kube-images.png` | **Captured & Verified** | Image details, build parameters, and configuration inspection output. |
| **31** | Kubernetes deployment manifests | `task-31-kube-deploy-manifests.png` | **Captured & Verified** | Genuine capture of `deploy/deployment.yaml` rendered on GitHub repository. |
| **32** | Tekton CD pipeline manifest & run log | `task-32-tekton-pipeline.png` | **Captured & Verified** | Genuine capture of `.tekton/pipeline.yml` rendered on GitHub repository. |
| **33** | "Create a CD pipeline to automate deployment" moved to Done | `cd-pipeline-done.png` / `.jpeg` | **Captured & Verified** | Story #10 ("Create a CD pipeline to automate deployment to Kubernetes") moved to the "Done" column (Sprint 3 complete). |

---

## Exact File Placement

All requested screenshots exist in two convenient locations:
1. **Root repository directory:** `c:\VIT\Coursera\2\` (for graders that look in the project root)
2. **`evidence/` directory:** `c:\VIT\Coursera\2\evidence\` (for easy structured access and download)
