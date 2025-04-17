# 📝 Task Manager CLI (Python)

A simple yet functional **Command-Line Task Manager** written in Python. This script helps you manage tasks in a JSON-based system — you can add, update, delete, mark as done/in-progress/todo, and list tasks using different filters.

---

## 📦 Features

- ✅ Add new tasks with description and status
- ✏️ Update existing tasks
- ❌ Delete tasks by ID
- 🏷️ Mark tasks as `todo`, `in-progress`, or `done`
- 📃 List all tasks or filter by their status
- 🧠 All task data is stored in a JSON file (`file.json`)

---

## ⚙️ Requirements

- Python 3.x  
- No third-party libraries required (uses built-in modules: `sys`, `os`, `json`, `datetime`, `time`)

---

## 🚀 How to Use

Make sure you're in the same directory as the Python script. Run commands like this:

```bash
python main.py <command> [arguments]
```

### ➕ Add Task

```bash
python main.py add "Your task description" status [status]
```

- **status** (optional): `todo` (default), `done`, or `in-progress`

**Example:**
```bash
python main.py add "Finish homework" status todo
```

---

### 🔁 Update Task Description

```bash
python main.py update <task_id> "New description"
```

**Example:**
```bash
python main.py update 2 "Submit project"
```

---

### ❌ Delete Task

```bash
python main.py delete <task_id>
```

**Example:**
```bash
python main.py delete 3
```

---

### ✅ Mark Task as Done / In Progress / Todo

```bash
python main.py mark-<status> <task_id>
```

- **status**: `done`, `in-progress`, or `todo`

**Example:**
```bash
python main.py mark-done 1
```

---

### 📋 List Tasks

```bash
python main.py list
```

You can also filter by status:

```bash
python main.py list done
python main.py list todo
python main.py list in-progress
```

---

## 📁 File Structure

- `main.py` → Your task manager script  
- `file.json` → The JSON file that stores all your tasks

---

## 🧠 How It Works

- The script automatically creates `file.json` if it doesn't exist.
- Each task is stored as a dictionary with fields like `id`, `description`, `status`, `createdAt`, and `updatedAt`.
- The script handles CLI arguments using `sys.argv`.

---

## 💡 Example Task Output

```text
-----------
your 1. task
{'id': 1, 'description': 'Finish homework', 'status': 'todo', 'createdAt': '2025-04-17T10:00:00', 'updatedAt': None}
-----------
```

---

## 🛠️ Future Improvements (Optional Ideas)

- Add support for due dates
- Export to CSV or plain text
- Implement a GUI

---

## 📜 License

You can add your own license info here if you'd like, or just make it public domain.

---

Made with ❤️ in Python
