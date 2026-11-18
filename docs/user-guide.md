# Student Task Manager – User Guide

## 1. Start the app

Open a terminal in the project folder and run:

```bash
python main.py
```

The main menu appears:

```
===== Student Task Manager =====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
```

Type the number of an option and press **Enter**.

## 2. Add a task (option 1)

Type a title, for example `Finish DevOps assignment`.

```
Task title: Finish DevOps assignment
Added: [ ] 1. Finish DevOps assignment
```

The title cannot be empty and can be at most 100 characters. If it is not valid you will see
`Error: Task title cannot be empty` and nothing is added.

## 3. Show tasks (option 2)

```
[x] 1. Finish DevOps assignment
[ ] 2. Revise SCD lecture 5
```

`[x]` means completed, `[ ]` means still to do. The number is the task ID.

## 4. Complete a task (option 3)

The app shows your tasks, then asks for an ID:

```
ID of the task to complete: 1
Completed: [x] 1. Finish DevOps assignment
```

If you type something that is not a number, or an ID that does not exist, you get an error
message and nothing changes.

## 5. Delete a task (option 4)

```
ID of the task to delete: 2
Deleted: Revise SCD lecture 5
```

Other tasks keep their IDs.

## 6. Exit (option 5)

Your tasks are saved automatically in `tasks.json` in the same folder, so they will be there
the next time you start the app. To start fresh, delete `tasks.json`.
