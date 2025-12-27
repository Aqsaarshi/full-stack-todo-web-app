# Using Claude Code with the Todo CLI Application

This document provides instructions on how to use Claude Code effectively with the Todo CLI Application project.

## Project Overview

The Todo CLI Application is a Python-based command-line tool for managing todo tasks in memory. It demonstrates fundamental CRUD operations (Create, Read, Update, Delete) along with task completion tracking.

## Project Structure

```
src/
├── models/
│   └── task.py          # Task model definition
├── services/
│   └── todo_service.py  # Business logic for todo operations
├── cli/
│   └── main.py          # CLI interface using argparse
└── lib/
    └── utils.py         # Utility functions

tests/
├── unit/
│   ├── test_task.py     # Unit tests for Task model
│   └── test_todo_service.py  # Unit tests for todo service
├── integration/
│   └── test_cli.py      # Integration tests for CLI
└── contract/
    └── test_api_contract.py  # Contract tests (if applicable)

specs_history/          # Specification files
README.md               # Setup and usage instructions
CLAUDE.md               # Claude Code usage instructions (this file)
CONSTITUTION.md         # Project guidelines
```

## Working with Claude Code

### 1. Adding New Features
When adding new features to the Todo CLI Application:
- Follow the existing modular design pattern
- Add new functionality to the appropriate module (models, services, or CLI)
- Write corresponding unit and integration tests
- Update documentation as needed

### 2. Modifying Existing Features
When modifying existing functionality:
- Review the existing tests to understand expected behavior
- Make changes to the relevant modules
- Update tests if the behavior changes
- Ensure all tests pass after your changes

### 3. Bug Fixes
When fixing bugs:
- First write a test that reproduces the bug
- Implement the fix
- Verify that the test now passes
- Run all existing tests to ensure no regressions

### 4. Testing
The project uses pytest for testing:
- Unit tests are in `tests/unit/`
- Integration tests are in `tests/integration/`
- Run all tests with: `pytest tests/`
- Run specific tests with: `pytest tests/unit/test_task.py`

### 5. Code Style
- Follow Python PEP 8 standards
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused on a single responsibility

## Key Implementation Details

### Task Model (`src/models/task.py`)
- Represents a single todo item
- Has attributes: ID, title, description, and status
- Includes validation for required fields

### Todo Service (`src/services/todo_service.py`)
- Contains all business logic for todo operations
- Handles in-memory storage of tasks
- Implements CRUD operations and status management

### CLI Interface (`src/cli/main.py`)
- Provides command-line interface using argparse
- Maps CLI commands to service methods
- Handles user input and displays output

## Common Tasks

### Adding a New Command
1. Add the command to the argument parser in `main.py`
2. Create a handler function for the command
3. Update the main dispatch logic to call your handler
4. Write tests for the new functionality
5. Update documentation if needed

### Extending the Task Model
1. Add new attributes to the Task class
2. Update the constructor and any relevant methods
3. Update the to_dict and from_dict methods if needed
4. Add tests for the new functionality
5. Update any CLI commands that might need to handle the new attributes

## Running the Application

To run the Todo CLI Application:
```bash
python src/cli/main.py [command] [arguments]
```

For help with available commands:
```bash
python src/cli/main.py --help
```