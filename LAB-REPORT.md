# Lab Report – Assignment 4: Student Task Manager with Git and GitHub

**Course:** DevOps for Cloud Computing (CSC418)
**Student:** Sharjeel Shahzad (FA23-BSE-170)
**Repository:** https://github.com/saadkhan-07/student-task-manager
**Release:** https://github.com/saadkhan-07/student-task-manager/releases/tag/v1.0.0

## 1. Git vs GitHub, and add / commit / push

**Git** is a version control tool that runs on my own computer. It records every change to
the project as commits, so I can see the history, go back, and work on branches.
**GitHub** is a website that hosts Git repositories online. It adds things Git does not have,
such as Issues, Pull Requests, code review, Actions and Releases, so a team can work together.

- `git add` puts changed files into the staging area – it chooses *what* goes into the next commit.
- `git commit` saves the staged changes as a snapshot in the local history, with a message.
- `git push` uploads my local commits to the remote repository on GitHub so others can see them.

## 2. Branches, Pull Requests and merge conflicts

**Branches** let me build a feature separately without breaking `main`. In this project each
feature (add-task validation, complete-task, delete-task, CI tests) had its own branch, so
the work could be tested and reviewed on its own.
**Pull Requests** are a request to merge a branch into `main`. They show the changed files,
let someone review and comment, run the automated tests, and link to the Issue being fixed.

A **merge conflict** happens when two branches change the *same lines* of the same file in
different ways, and Git cannot decide which version to keep. In Part D both
`status/in-progress` and `status/testing` changed the line `Project status: Planning`. After
the first branch was merged, merging the second one stopped with a conflict. I opened
`README.md`, looked at the `<<<<<<<`, `=======` and `>>>>>>>` markers, kept both pieces of
information in one line, removed the markers, then ran `git add` and `git commit`.

## 3. fetch vs pull, merge vs rebase

- `git fetch` downloads new commits from GitHub but does **not** change my working files.
  `git pull` = `git fetch` + merge, so it downloads **and** updates my current branch.
- `git merge` joins two branches and creates a merge commit, keeping the full history of both.
  `git rebase` moves my commits so they sit on top of the other branch, giving a straight,
  cleaner history, but it rewrites commits, so it should not be used on shared branches.

## 4. How Issues and Actions help a team

**GitHub Issues** are a shared to-do list. Each piece of work (feature, bug, documentation)
gets a description, a label and an owner, and PRs can close them automatically
(`Closes #1`). Everyone can see what is planned, in progress and done.
**GitHub Actions** runs the tests automatically on every push and pull request. Problems are
caught before merging – a red ❌ check blocks a broken change, and a green ✅ check shows the
change is safe.

## 5. A difficulty I faced and how I solved it

My first GitHub Actions run failed. The log showed `test_delete_task` failed with
`AssertionError: 1 != 2`. The app was correct – my test was wrong: after adding two tasks and
deleting one, it expected 2 tasks to remain instead of 1. I fixed the expected value, pushed
again to the same PR branch, and the next run passed with all 6 tests green. This showed me
how CI catches mistakes before they reach `main`.

## Summary of work

| Requirement | Evidence |
|---|---|
| 12+ meaningful commits | `git log` – 25+ commits on `main` |
| 3 feature branches | `feature/add-task`, `feature/complete-task`, `feature/delete-task` (+ `feature/ci-tests`) |
| 4+ Issues with labels | Issues #1–#5 |
| 5 merged Pull Requests | PRs #6, #7, #8, #9, #10 |
| 1 resolved conflict | Merge of `status/testing` into `main` |
| 3+ automated tests | 6 tests in `tests/test_task_manager.py` |
| 1 workflow | `.github/workflows/tests.yml` (one failed run, then successful runs) |
| 1 release | `v1.0.0` |

Screenshots of each step are in the [`lab-evidence/`](lab-evidence/) folder.
