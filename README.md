# The Matrix - Welcome to the Real World of Data Engineering

## Overview
The Matrix explores foundational data engineering infrastructure tools in Python 3.10+. Set in a Matrix-themed simulation, this subject covers environment isolation using virtual environments (`venv`), modern dependency management tools (`pip` vs. `Poetry`), data synthesis/visualization using `numpy`, `pandas`, and `matplotlib`, as well as secure configuration practices through environment variables and `.env` files via `python-dotenv`.

---

## Technical Requirements & Guidelines

* Language: Python 3.10+
* Code Style: Strict adherence to flake8 linter standards.
* Type Hinting: Mandatory across all functions (mypy compliant). Import errors in `ex1/` are exceptionally permitted for dependency checks.
* Constraints:
  * Modifying system installations is strictly discouraged; all development must support virtual environment isolation.
  * Virtual environments (e.g., `matrix_env/`, `.venv/`) and `.env` files containing live credentials must NEVER be committed to Git.
  * Data in `ex1/` must be generated programmatically via `numpy` (no hardcoded lists or `range()`).
  * `ex2/` must use `python-dotenv` for loading environment files rather than manual custom file parsers.

---

## Exercises Summary

| Part | Concept | Key Files | Description |
| :--- | :--- | :--- | :--- |
| Exercise 0: Entering the Matrix | Environment Detection & Isolation | `ex0/construct.py` | Detects whether execution occurs within a virtual environment, reporting site-packages paths or offering venv activation instructions. |
| Exercise 1: Loading Programs | Dependency Management & Data Generation | `ex1/loading.py`, `ex1/requirements.txt`, `ex1/pyproject.toml` | Verifies and loads external dependencies (`pandas`, `numpy`, `matplotlib`, optional `requests`), synthesizes data, creates `matrix_analysis.png`, and compares `pip` vs. `Poetry`. |
| Exercise 2: Accessing the Mainframe | Configuration & Environment Security | `ex2/oracle.py`, `ex2/requirements.txt`, `ex2/.env.example`, `ex2/.gitignore` | Loads system configuration (`MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, etc.) using `python-dotenv`, supporting development/production overrides without leaking secrets. |

---

## Exercise Details

### Exercise 0: Entering the Matrix
* Concepts: System paths (`sys.prefix`, `sys.base_prefix`), site-packages locations (`site`), CLI user guidance.
* Key Mechanics:
  * Inspects `sys.prefix != sys.base_prefix` or `sys.real_prefix` to determine virtual environment status.
  * When un-isolated: Displays warning and shell instructions to create (`python3 -m venv matrix_env`) and activate (`source matrix_env/bin/activate`) a venv.
  * When isolated: Confirms active environment name, path, and `site-packages` directory.

### Exercise 1: Loading Programs
* Concepts: Package management, dynamic import checking (`importlib`), numerical simulation, data visualization.
* Key Mechanics:
  * Dynamic Import Check: Tests availability of `pandas`, `numpy`, `matplotlib` (and optional `requests`), gracefully outputting version details or installation instructions if missing.
  * Data Generation: Synthesizes Matrix data arrays exclusively using `numpy` functions.
  * Processing & Export: Converts raw arrays into a `pandas.DataFrame`, processes statistics, and saves visual output to `matrix_analysis.png` via `matplotlib`.
  * Dependency Specifications: Configures `requirements.txt` for `pip` and `pyproject.toml` for `Poetry`.

### Exercise 2: Accessing the Mainframe
* Concepts: Environment variables (`os.environ`), `.env` secrets management, runtime environment modes.
* Key Mechanics:
  * Secure Config: Reads `MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, `LOG_LEVEL`, and `ZION_ENDPOINT`.
  * Dotenv Loading: Uses `python-dotenv` to populate environment variables from `.env`.
  * Precedence & Overrides: System/CLI environment variables override `.env` values (e.g., `MATRIX_MODE=production python3 oracle.py`).
  * Security Validation: Ensures `.env` is listed in `.gitignore` while `.env.example` provides non-sensitive template keys.

---

## Testing & Quality Assurance

Verify strict compliance with formatting standards (flake8) and static typing (mypy):

# Check formatting standards across all exercises
flake8 ex0/construct.py ex1/loading.py ex2/oracle.py

# Check static typing
mypy ex0/construct.py ex1/loading.py ex2/oracle.py

# Test Exercise 0 outside and inside virtual environment
python3 ex0/construct.py
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 ex0/construct.py

# Test Exercise 1 via pip and Poetry
pip install -r ex1/requirements.txt
python3 ex1/loading.py

poetry install
poetry run python ex1/loading.py

# Test Exercise 2 environment configuration overrides
cp ex2/.env.example ex2/.env
python3 ex2/oracle.py
MATRIX_MODE=production API_KEY=secret123 python3 ex2/oracle.py
