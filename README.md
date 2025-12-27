# Todo CLI Application

A simple command-line interface application for managing todo tasks in memory.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with their status indicators
- Update task titles and descriptions
- Delete tasks
- Mark tasks as complete or incomplete

## Requirements

- Python 3.13+

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. The application is ready to use (no additional installation required)

## Usage

### Interactive Mode (Recommended)
Run the application in interactive mode where tasks persist in memory during the session:

```bash
python src/cli/main.py
```

Then use commands within the interactive session:
- `add "Task Title" "Optional Description"` - Add a new task
- `view` - View all tasks
- `update [task_id] --title "New Title" --description "New Description"` - Update a task
- `delete [task_id]` - Delete a task
- `mark-complete [task_id]` - Mark task as complete
- `mark-incomplete [task_id]` - Mark task as incomplete
- `help` - Show available commands
- `quit` or `exit` - Exit the application

### Standalone Mode (Original)
Run individual commands (tasks will not persist between executions):

```bash
python src/cli/main.py add "Task Title" "Optional Description"
python src/cli/main.py view
python src/cli/main.py update [task_id] --title "New Title" --description "New Description"
python src/cli/main.py delete [task_id]
python src/cli/main.py mark-complete [task_id]
python src/cli/main.py mark-incomplete [task_id]
```

## Example Usage (Interactive Mode)

```
python src/cli/main.py
todo> add "Buy groceries" "Milk, eggs, bread"
Task added successfully with ID: 1
todo> view
Your Todo List:
[O] 1. Buy groceries
      Description: Milk, eggs, bread

todo> update 1 --title "Buy groceries and cook dinner"
Task 1 updated successfully
todo> mark-complete 1
Task 1 marked as complete
todo> view
Your Todo List:
[X] 1. Buy groceries and cook dinner
      Description: Milk, eggs, bread

todo> quit
Goodbye!
```

## Architecture

The application follows a modular design with clear separation of concerns:

- `src/models/task.py`: Defines the Task entity
- `src/services/todo_service.py`: Contains business logic for todo operations
- `src/cli/main.py`: Implements the command-line interface
- `src/lib/utils.py`: Contains utility functions

## Testing

To run the tests:
```bash
pip install pytest
pytest tests/
```

## License

[Specify your license here]# The-Evolution-of-Todo-app
