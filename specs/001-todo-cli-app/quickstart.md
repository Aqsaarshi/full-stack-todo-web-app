# Quickstart Guide: Todo CLI App

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Clone or download the repository
3. Navigate to the project directory

## Running the Application

To run the Todo CLI application:

```bash
cd src/cli
python main.py [command] [options]
```

## Available Commands

### Add a Task
```bash
python main.py add "Task Title" "Optional Description"
```

### View All Tasks
```bash
python main.py view
```

### Update a Task
```bash
python main.py update [task_id] --title "New Title" --description "New Description"
```

### Delete a Task
```bash
python main.py delete [task_id]
```

### Mark Task as Complete
```bash
python main.py mark-complete [task_id]
```

### Mark Task as Incomplete
```bash
python main.py mark-incomplete [task_id]
```

## Example Usage

```bash
# Add a new task
python main.py add "Buy groceries" "Milk, eggs, bread"

# View all tasks
python main.py view

# Update a task (assuming it has ID 1)
python main.py update 1 --title "Buy groceries and cook dinner"

# Mark task as complete
python main.py mark-complete 1

# Delete a task
python main.py delete 1
```

## Development

To run tests:
```bash
pytest tests/
```