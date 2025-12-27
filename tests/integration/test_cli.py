"""
Integration tests for the CLI add command.
"""
import sys
import subprocess
import os
from pathlib import Path


class TestCLIAddCommand:
    """Test cases for the CLI add command."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # For this simple CLI app, we're testing the actual CLI behavior
        self.cli_path = Path("src/cli/main.py")
        self.original_argv = sys.argv[:]

    def teardown_method(self):
        """Tear down test fixtures after each test method."""
        sys.argv = self.original_argv
    
    def test_add_task_with_title_only(self, capsys):
        """Test adding a task with only a title."""
        # This test would require mocking or a more complex setup
        # For now, we'll test the functionality through direct import
        from src.services.todo_service import TodoService
        
        service = TodoService()
        task = service.add_task("Buy groceries")
        
        assert task.title == "Buy groceries"
        assert task.description == ""
        assert len(service.get_all_tasks()) == 1
    
    def test_add_task_with_title_and_description(self, capsys):
        """Test adding a task with both title and description."""
        from src.services.todo_service import TodoService
        
        service = TodoService()
        task = service.add_task("Buy groceries", "Milk, eggs, bread")
        
        assert task.title == "Buy groceries"
        assert task.description == "Milk, eggs, bread"
        assert len(service.get_all_tasks()) == 1
    
    def test_add_task_assigns_unique_ids(self, capsys):
        """Test that adding multiple tasks assigns unique IDs."""
        from src.services.todo_service import TodoService
        
        service = TodoService()
        task1 = service.add_task("First task")
        task2 = service.add_task("Second task")
        
        assert task1.id == 1
        assert task2.id == 2
        assert len(service.get_all_tasks()) == 2
    
    def test_add_task_empty_title_fails(self, capsys):
        """Test that adding a task with empty title fails."""
        from src.services.todo_service import TodoService
        
        service = TodoService()
        
        try:
            service.add_task("")
            assert False, "Expected ValueError was not raised"
        except ValueError as e:
            assert "Title cannot be empty" in str(e)
    
    def test_cli_add_command_execution(self):
        """Test that the CLI add command can be executed."""
        # This would test the actual CLI command execution
        # For now, we'll just verify the script can be imported without errors
        import src.cli.main
        assert hasattr(src.cli.main, 'main')
        assert hasattr(src.cli.main, 'create_parser')


class TestCLIViewCommand:
    """Test cases for the CLI view command."""

    def test_view_empty_task_list(self):
        """Test viewing an empty task list."""
        from src.services.todo_service import TodoService

        # Create a service with no tasks
        service = TodoService()

        # Capture the output of the view functionality
        tasks = service.get_all_tasks()

        assert len(tasks) == 0

    def test_view_single_task(self):
        """Test viewing a single task."""
        from src.services.todo_service import TodoService
        from src.models.task import TaskStatus

        service = TodoService()
        service.add_task("Test Task", "Test Description")

        tasks = service.get_all_tasks()

        assert len(tasks) == 1
        assert tasks[0].title == "Test Task"
        assert tasks[0].description == "Test Description"
        assert tasks[0].status == TaskStatus.INCOMPLETE

    def test_view_multiple_tasks(self):
        """Test viewing multiple tasks."""
        from src.services.todo_service import TodoService
        from src.models.task import TaskStatus

        service = TodoService()
        service.add_task("First Task", "Description 1")
        service.add_task("Second Task", "Description 2")
        service.add_task("Third Task")  # No description

        tasks = service.get_all_tasks()

        assert len(tasks) == 3
        assert tasks[0].title == "First Task"
        assert tasks[1].title == "Second Task"
        assert tasks[2].title == "Third Task"
        assert tasks[0].description == "Description 1"
        assert tasks[1].description == "Description 2"
        assert tasks[2].description == ""
        assert all(task.status == TaskStatus.INCOMPLETE for task in tasks)

    def test_view_tasks_with_different_statuses(self):
        """Test viewing tasks with different statuses."""
        from src.services.todo_service import TodoService
        from src.models.task import TaskStatus

        service = TodoService()
        task1 = service.add_task("Incomplete Task")
        task2 = service.add_task("Complete Task")

        # Mark the second task as complete
        service.mark_complete(task2.id)

        tasks = service.get_all_tasks()

        assert len(tasks) == 2
        incomplete_tasks = [task for task in tasks if task.status == TaskStatus.INCOMPLETE]
        complete_tasks = [task for task in tasks if task.status == TaskStatus.COMPLETE]

        assert len(incomplete_tasks) == 1
        assert len(complete_tasks) == 1
        assert incomplete_tasks[0].title == "Incomplete Task"
        assert complete_tasks[0].title == "Complete Task"


class TestCLIMarkCompleteCommand:
    """Test cases for the CLI mark-complete command."""

    def test_mark_complete_existing_task(self):
        """Test marking an existing task as complete."""
        from src.services.todo_service import TodoService
        from src.models.task import TaskStatus

        service = TodoService()
        task = service.add_task("Test Task")

        # Mark the task as complete
        result = service.mark_complete(task.id)

        assert result is True
        assert task.status == TaskStatus.COMPLETE

    def test_mark_complete_nonexistent_task(self):
        """Test marking a non-existent task as complete."""
        from src.services.todo_service import TodoService

        service = TodoService()

        # Try to mark a non-existent task as complete
        result = service.mark_complete(999)

        assert result is False

    def test_mark_complete_already_complete_task(self):
        """Test marking a task that is already complete."""
        from src.services.todo_service import TodoService
        from src.models.task import TaskStatus

        service = TodoService()
        task = service.add_task("Test Task")

        # Mark as complete
        result1 = service.mark_complete(task.id)
        # Mark as complete again
        result2 = service.mark_complete(task.id)

        assert result1 is True
        assert result2 is True
        assert task.status == TaskStatus.COMPLETE


class TestCLIMarkIncompleteCommand:
    """Test cases for the CLI mark-incomplete command."""

    def test_mark_incomplete_existing_task(self):
        """Test marking an existing task as incomplete."""
        from src.services.todo_service import TodoService
        from src.models.task import TaskStatus

        service = TodoService()
        task = service.add_task("Test Task")
        service.mark_complete(task.id)  # First mark as complete

        # Mark the task as incomplete
        result = service.mark_incomplete(task.id)

        assert result is True
        assert task.status == TaskStatus.INCOMPLETE

    def test_mark_incomplete_nonexistent_task(self):
        """Test marking a non-existent task as incomplete."""
        from src.services.todo_service import TodoService

        service = TodoService()

        # Try to mark a non-existent task as incomplete
        result = service.mark_incomplete(999)

        assert result is False

    def test_mark_incomplete_already_incomplete_task(self):
        """Test marking a task that is already incomplete."""
        from src.services.todo_service import TodoService
        from src.models.task import TaskStatus

        service = TodoService()
        task = service.add_task("Test Task")

        # Task is already incomplete by default
        result = service.mark_incomplete(task.id)

        assert result is True
        assert task.status == TaskStatus.INCOMPLETE


class TestCLIUpdateCommand:
    """Test cases for the CLI update command."""

    def test_update_task_title_only(self):
        """Test updating only the title of a task."""
        from src.services.todo_service import TodoService

        service = TodoService()
        task = service.add_task("Original Title", "Original Description")

        # Update the task title
        result = service.update_task(task.id, title="New Title")

        assert result is True
        assert task.title == "New Title"
        assert task.description == "Original Description"

    def test_update_task_description_only(self):
        """Test updating only the description of a task."""
        from src.services.todo_service import TodoService

        service = TodoService()
        task = service.add_task("Original Title", "Original Description")

        # Update the task description
        result = service.update_task(task.id, description="New Description")

        assert result is True
        assert task.title == "Original Title"
        assert task.description == "New Description"

    def test_update_task_both_title_and_description(self):
        """Test updating both title and description of a task."""
        from src.services.todo_service import TodoService

        service = TodoService()
        task = service.add_task("Original Title", "Original Description")

        # Update both title and description
        result = service.update_task(task.id, title="New Title", description="New Description")

        assert result is True
        assert task.title == "New Title"
        assert task.description == "New Description"

    def test_update_nonexistent_task(self):
        """Test updating a non-existent task."""
        from src.services.todo_service import TodoService

        service = TodoService()

        # Try to update a non-existent task
        result = service.update_task(999, title="New Title")

        assert result is False

    def test_update_task_empty_title_fails(self):
        """Test that updating a task with empty title fails."""
        from src.services.todo_service import TodoService

        service = TodoService()
        task = service.add_task("Original Title")

        try:
            service.update_task(task.id, title="")
            assert False, "Expected ValueError was not raised"
        except ValueError as e:
            assert "Title cannot be empty" in str(e)

    def test_update_task_preserves_status(self):
        """Test that updating a task preserves its status."""
        from src.services.todo_service import TodoService
        from src.models.task import TaskStatus

        service = TodoService()
        task = service.add_task("Original Title")
        service.mark_complete(task.id)  # Mark as complete

        # Update the task
        result = service.update_task(task.id, title="New Title")

        assert result is True
        assert task.status == TaskStatus.COMPLETE
        assert task.title == "New Title"


class TestCLIDeleteCommand:
    """Test cases for the CLI delete command."""

    def test_delete_existing_task(self):
        """Test deleting an existing task."""
        from src.services.todo_service import TodoService

        service = TodoService()
        task = service.add_task("Test Task")

        # Delete the task
        result = service.delete_task(task.id)

        assert result is True
        assert len(service.get_all_tasks()) == 0

    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task."""
        from src.services.todo_service import TodoService

        service = TodoService()

        # Try to delete a non-existent task
        result = service.delete_task(999)

        assert result is False
        assert len(service.get_all_tasks()) == 0

    def test_delete_task_from_multiple_tasks(self):
        """Test deleting one task from multiple tasks."""
        from src.services.todo_service import TodoService

        service = TodoService()
        task1 = service.add_task("First Task")
        task2 = service.add_task("Second Task")
        task3 = service.add_task("Third Task")

        # Delete the second task
        result = service.delete_task(task2.id)

        assert result is True
        remaining_tasks = service.get_all_tasks()
        assert len(remaining_tasks) == 2
        assert task1 in remaining_tasks
        assert task3 in remaining_tasks
        assert task2 not in remaining_tasks

    def test_delete_preserves_other_task_properties(self):
        """Test that deleting a task preserves properties of other tasks."""
        from src.services.todo_service import TodoService
        from src.models.task import TaskStatus

        service = TodoService()
        task1 = service.add_task("First Task", "Description 1")
        task2 = service.add_task("Second Task", "Description 2")
        task3 = service.add_task("Third Task", "Description 3")

        # Mark task1 as complete
        service.mark_complete(task1.id)

        # Delete task2
        result = service.delete_task(task2.id)

        assert result is True

        # Check that other tasks preserved their properties
        remaining_tasks = {task.id: task for task in service.get_all_tasks()}
        assert len(remaining_tasks) == 2
        assert remaining_tasks[1].title == "First Task"
        assert remaining_tasks[1].description == "Description 1"
        assert remaining_tasks[1].status == TaskStatus.COMPLETE
        assert remaining_tasks[3].title == "Third Task"
        assert remaining_tasks[3].description == "Description 3"
        assert remaining_tasks[3].status == TaskStatus.INCOMPLETE