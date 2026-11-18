# student-task-manager

![Python tests](https://github.com/saadkhan-07/student-task-manager/actions/workflows/tests.yml/badge.svg)

A small Python console application that helps students keep track of their tasks.
Built for **DevOps for Cloud Computing (CSC418) – Lab Assignment 4** to practise a complete
Git and GitHub workflow: commits, branches, pull requests, merge conflicts, automated tests
and releases.

Project status: Complete – v1.0.0 released (all features implemented and tested)

## Features

- **Add tasks** – titles are trimmed; empty, whitespace-only and over-100-character titles are rejected
- **Show tasks** – lists every task with its ID and a `[x]` / `[ ]` completion mark
- **Complete tasks** – mark a task as done by entering its ID
- **Delete tasks** – remove a task by its ID; other tasks keep their IDs
- **Saved automatically** – tasks are stored in `tasks.json` so they are still there next time
- **Automated tests** – Python `unittest` tests run on GitHub Actions for every push and pull request to `main`

## Project structure

```
student-task-manager/
├── main.py                  # console menu (entry point)
├── task_manager.py          # Task model and TaskManager logic
├── tests/
│   └── test_task_manager.py # unit tests
├── docs/
│   └── user-guide.md        # short user guide
├── lab-evidence/            # screenshots of key steps
├── .github/workflows/
│   └── tests.yml            # GitHub Actions workflow
├── LAB-REPORT.md
└── LICENSE                  # MIT
```

## Setup

Requirements: Python 3.8 or newer. No extra packages are needed.

```bash
git clone https://github.com/saadkhan-07/student-task-manager.git
cd student-task-manager
```

## Usage

```bash
python main.py
```

Then choose an option from the menu:

```
===== Student Task Manager =====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
```

See [docs/user-guide.md](docs/user-guide.md) for a step-by-step example.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

The same command runs automatically in GitHub Actions
(`.github/workflows/tests.yml`) on every push to `main` and every pull request to `main`.

## License

Released under the [MIT License](LICENSE).
