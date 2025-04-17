# Task Manager CLI

A simple command-line task manager written in Python. This script allows you to perform various actions on a list of tasks stored in a JSON file. You can add, update, delete, mark, or list tasks.

## Features

- **Add tasks**: Add new tasks with a description and status (default status is "todo").
- **Update tasks**: Modify the description of a task.
- **Delete tasks**: Remove tasks from the list.
- **Mark tasks**: Change the status of a task (options: `todo`, `done`, `in-progress`).
- **List tasks**: View all tasks or filter by their status.

## Prerequisites

- Python 3.x
- No external libraries are required (the script uses built-in libraries like `sys`, `os`, `json`, `datetime`, and `time`).

## Usage

Run the script from the command line with the following commands:

### Add a task
```bash
python task_manager.py add <description> [status]
