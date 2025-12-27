# CLI Contract: Todo CLI App

## Command Structure

The application follows the structure:
```
python main.py <command> [arguments] [options]
```

## Commands Specification

### 1. Add Task
- **Command**: `add`
- **Arguments**:
  - `title` (required): String - The title of the task
  - `description` (optional): String - Additional details about the task
- **Options**: None
- **Output**: Success message with the created task ID
- **Example**: `python main.py add "Buy groceries" "Milk, eggs, bread"`
- **Success Response**: "Task added successfully with ID: [id]"
- **Error Responses**:
  - "Error: Title cannot be empty"
  - "Error: Invalid input parameters"

### 2. View Tasks
- **Command**: `view`
- **Arguments**: None
- **Options**: None
- **Output**: List of all tasks with ID, title, description, and status
- **Example**: `python main.py view`
- **Success Response**: Formatted list of all tasks
- **Error Responses**: None (empty list is valid)

### 3. Update Task
- **Command**: `update`
- **Arguments**:
  - `id` (required): Integer - The ID of the task to update
- **Options**:
  - `--title` (optional): String - New title for the task
  - `--description` (optional): String - New description for the task
- **Output**: Success message
- **Example**: `python main.py update 1 --title "Updated title"`
- **Success Response**: "Task [id] updated successfully"
- **Error Responses**:
  - "Error: Task with ID [id] does not exist"
  - "Error: Invalid task ID"

### 4. Delete Task
- **Command**: `delete`
- **Arguments**:
  - `id` (required): Integer - The ID of the task to delete
- **Options**: None
- **Output**: Success message
- **Example**: `python main.py delete 1`
- **Success Response**: "Task [id] deleted successfully"
- **Error Responses**:
  - "Error: Task with ID [id] does not exist"
  - "Error: Invalid task ID"

### 5. Mark Complete
- **Command**: `mark-complete`
- **Arguments**:
  - `id` (required): Integer - The ID of the task to mark as complete
- **Options**: None
- **Output**: Success message
- **Example**: `python main.py mark-complete 1`
- **Success Response**: "Task [id] marked as complete"
- **Error Responses**:
  - "Error: Task with ID [id] does not exist"
  - "Error: Invalid task ID"

### 6. Mark Incomplete
- **Command**: `mark-incomplete`
- **Arguments**:
  - `id` (required): Integer - The ID of the task to mark as incomplete
- **Options**: None
- **Output**: Success message
- **Example**: `python main.py mark-incomplete 1`
- **Success Response**: "Task [id] marked as incomplete"
- **Error Responses**:
  - "Error: Task with ID [id] does not exist"
  - "Error: Invalid task ID"

## Common Error Responses

- "Error: Invalid command. Use 'python main.py --help' for available commands."
- "Error: Missing required argument(s)."
- "Error: Invalid argument format."
- "Error: An unexpected error occurred."

## Exit Codes

- `0`: Success
- `1`: General error
- `2`: Invalid command-line usage