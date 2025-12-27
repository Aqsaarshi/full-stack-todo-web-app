"""
Interactive Todo Terminal Application.
"""
import sys
import os
from typing import Optional

# Get the directory containing this script (cli directory)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up two levels to reach the src directory
src_dir = os.path.join(current_dir, '..', '..')
# Add src to the Python path so we can import from it
sys.path.insert(0, os.path.abspath(src_dir))

from src.services.todo_service import TodoService
from src.models.task import Task


def print_help():
    """Print the help message with available commands."""
    print("\nTodo Terminal Application - Available Commands:")
    print("  add <title> [description]    - Add a new task")
    print("  view                         - View all tasks")
    print("  update <id> --title <title> --description <description> - Update a task")
    print("  delete <id>                  - Delete a task")
    print("  mark-complete <id>           - Mark task as complete")
    print("  mark-incomplete <id>         - Mark task as incomplete")
    print("  help                         - Show this help message")
    print("  quit                         - Exit the application")
    print()


def parse_command(user_input: str) -> tuple:
    """Parse the user input into command and arguments."""
    parts = user_input.strip().split()
    if not parts:
        return None, []

    command = parts[0].lower()
    args = parts[1:]

    return command, args


def handle_add(service: TodoService, args: list) -> None:
    """Handle the add command."""
    if len(args) < 1:
        print("Error: Add command requires a title. Usage: add <title> [description]")
        return

    title = args[0]
    description = " ".join(args[1:]) if len(args) > 1 else ""

    try:
        task = service.add_task(title, description)
        print(f"Task added successfully with ID: {task.id}")
    except ValueError as e:
        print(f"Error: {e}")


def handle_view(service: TodoService, args: list) -> None:
    """Handle the view command."""
    tasks = service.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("Your Todo List:")
    for task in tasks:
        status_indicator = "X" if task.status.name == "COMPLETE" else "O"
        print(f"[{status_indicator}] {task.id}. {task.title}")
        if task.description:
            print(f"      Description: {task.description}")
        print()


def handle_update(service: TodoService, args: list) -> None:
    """Handle the update command."""
    if len(args) < 1:
        print("Error: Update command requires an ID. Usage: update <id> --title <title> --description <description>")
        return

    try:
        task_id = int(args[0])
    except ValueError:
        print("Error: Task ID must be a number")
        return

    # Parse additional arguments for title and description
    title = None
    description = None

    i = 1
    while i < len(args):
        if args[i] == "--title" and i + 1 < len(args):
            title = args[i + 1]
            i += 2
        elif args[i] == "--description" and i + 1 < len(args):
            description = args[i + 1]
            i += 2
        else:
            print(f"Error: Unknown argument '{args[i]}'")
            return

    try:
        success = service.update_task(task_id, title, description)
        if success:
            print(f"Task {task_id} updated successfully")
        else:
            print(f"Error: Task with ID {task_id} does not exist")
    except ValueError as e:
        print(f"Error: {e}")


def handle_delete(service: TodoService, args: list) -> None:
    """Handle the delete command."""
    if len(args) < 1:
        print("Error: Delete command requires an ID. Usage: delete <id>")
        return

    try:
        task_id = int(args[0])
        success = service.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Error: Task with ID {task_id} does not exist")
    except ValueError:
        print("Error: Task ID must be a number")


def handle_mark_complete(service: TodoService, args: list) -> None:
    """Handle the mark-complete command."""
    if len(args) < 1:
        print("Error: Mark-complete command requires an ID. Usage: mark-complete <id>")
        return

    try:
        task_id = int(args[0])
        success = service.mark_complete(task_id)
        if success:
            print(f"Task {task_id} marked as complete")
        else:
            print(f"Error: Task with ID {task_id} does not exist")
    except ValueError:
        print("Error: Task ID must be a number")


def handle_mark_incomplete(service: TodoService, args: list) -> None:
    """Handle the mark-incomplete command."""
    if len(args) < 1:
        print("Error: Mark-incomplete command requires an ID. Usage: mark-incomplete <id>")
        return

    try:
        task_id = int(args[0])
        success = service.mark_incomplete(task_id)
        if success:
            print(f"Task {task_id} marked as incomplete")
        else:
            print(f"Error: Task with ID {task_id} does not exist")
    except ValueError:
        print("Error: Task ID must be a number")


def main() -> None:
    """Main entry point for the interactive terminal application."""
    print("Welcome to the Todo Terminal Application!")
    print("Type 'help' for available commands or 'quit' to exit.")

    # Initialize the service (this will persist throughout the session)
    service = TodoService()

    while True:
        try:
            user_input = input("\ntodo> ").strip()

            if not user_input:
                continue

            command, args = parse_command(user_input)

            if command in ["quit", "exit", "q"]:
                print("Goodbye!")
                break
            elif command == "help":
                print_help()
            elif command == "add":
                handle_add(service, args)
            elif command == "view":
                handle_view(service, args)
            elif command == "update":
                handle_update(service, args)
            elif command == "delete":
                handle_delete(service, args)
            elif command == "mark-complete":
                handle_mark_complete(service, args)
            elif command == "mark-incomplete":
                handle_mark_incomplete(service, args)
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()