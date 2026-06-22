# Instructor Guide

## Expected Solution
- **Conflict 1 (config.py)**: Students should merge `MAX_SPEED = 2.0` and `MAX_SPEED = 1.0`. A sensible resolution is parameterizing it or choosing a safe middle ground (e.g., 1.5).
- **Conflict 2 (README.md)**: Students need to keep both appended sections ("Navigation Module" and "Configuration").
- **CI Fix**: `test_controller.py` has an assertion `apply_speed(2.0) == 999.0`. Students must change this back to test the correct boundary logic.

## Grading Rubric
- Conflict Resolution: 30%
- PR Review Participation: 20%
- CI/CD Repair: 20%
- Git Usage Quality: 15%
- Documentation: 15%
