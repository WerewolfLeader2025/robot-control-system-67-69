# Git Collaborative Development Assignment

Welcome to the Robot Control System project! The main branch is currently missing several key features developed by different teams. Your objective is to integrate these branches, resolve conflicts, review code, and fix the broken CI/CD pipeline.

## Instructions
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Create a Fix Branch**: Create a new branch named `integration-fix` from `main`.
3. **Merge Branches & Resolve Conflicts**:
   - Merge `feature-navigation` into your branch.
   - Merge `feature-safety` into your branch. You will encounter a merge conflict in `src/config.py`.
   - Merge `feature-config` into your branch. You will encounter a merge conflict in `README.md`.
   - **Resolve all conflicts logically** and commit the resolutions.
4. **Address Code Review Comments**: Read `REVIEW_COMMENTS.md` and make the requested changes.
5. **Repair CI Pipeline**: The `feature-safety` branch introduced a failing unit test. Fix the test in `tests/test_controller.py` so the GitHub Actions pipeline passes.
6. **Submit PR**: Push your `integration-fix` branch to GitHub and create a Pull Request against `main`.
7. **Document Teamwork**: Fill out the `TEAMWORK.md` file detailing who did what and how conflicts were resolved. Include this in your PR.
