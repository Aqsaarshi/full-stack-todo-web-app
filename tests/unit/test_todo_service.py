"""
Unit tests for the TodoService add_task and get_all_tasks functionality.
"""
import pytest

from src.services.todo_service import TodoService
from src.models.task import Task, TaskStatus


class TestTodoServiceAddTask:
    """Test cases for the TodoService add_task functionality."""

    def test_add_task_with_title_only(self):
        """Test adding a task with only a title."""
        service = TodoService()

        task = service.add_task("Test Task")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.status == TaskStatus.INCOMPLETE
        assert len(service.get_all_tasks()) == 1

    def test_add_task_with_title_and_description(self):
        """Test adding a task with both title and description."""
        service = TodoService()

        task = service.add_task("Test Task", "Test Description")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status == TaskStatus.INCOMPLETE
        assert len(service.get_all_tasks()) == 1

    def test_add_multiple_tasks_increments_id(self):
        """Test that adding multiple tasks increments the ID correctly."""
        service = TodoService()

        task1 = service.add_task("First Task")
        task2 = service.add_task("Second Task")

        assert task1.id == 1
        assert task2.id == 2
        assert len(service.get_all_tasks()) == 2

    def test_add_task_empty_title_raises_error(self):
        """Test that adding a task with empty title raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task("")

    def test_add_task_none_title_raises_error(self):
        """Test that adding a task with None title raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task(None)

    def test_add_task_whitespace_title_raises_error(self):
        """Test that adding a task with whitespace-only title raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task("   ")

    def test_add_task_assigns_unique_ids(self):
        """Test that each added task gets a unique ID."""
        service = TodoService()

        task1 = service.add_task("First Task")
        task2 = service.add_task("Second Task")
        task3 = service.add_task("Third Task")

        ids = [task1.id, task2.id, task3.id]
        assert len(ids) == len(set(ids))  # All IDs should be unique
        assert ids == [1, 2, 3]  # IDs should be sequential starting from 1

    def test_add_task_defaults_to_incomplete(self):
        """Test that added tasks default to incomplete status."""
        service = TodoService()

        task = service.add_task("Test Task")

        assert task.status == TaskStatus.INCOMPLETE


class TestTodoServiceGetAllTasks:
    """Test cases for the TodoService get_all_tasks functionality."""

    def test_get_all_tasks_empty_service(self):
        """Test getting all tasks when service is empty."""
        service = TodoService()

        tasks = service.get_all_tasks()

        assert len(tasks) == 0
        assert tasks == []

    def test_get_all_tasks_single_task(self):
        """Test getting all tasks when service has one task."""
        service = TodoService()
        expected_task = service.add_task("Test Task")

        tasks = service.get_all_tasks()

        assert len(tasks) == 1
        assert tasks[0] == expected_task

    def test_get_all_tasks_multiple_tasks(self):
        """Test getting all tasks when service has multiple tasks."""
        service = TodoService()
        expected_task1 = service.add_task("First Task")
        expected_task2 = service.add_task("Second Task")
        expected_task3 = service.add_task("Third Task")

        tasks = service.get_all_tasks()

        assert len(tasks) == 3
        assert expected_task1 in tasks
        assert expected_task2 in tasks
        assert expected_task3 in tasks

    def test_get_all_tasks_returns_copy(self):
        """Test that get_all_tasks returns a copy of the internal list."""
        service = TodoService()
        service.add_task("Test Task")

        tasks = service.get_all_tasks()
        original_length = len(tasks)

        # Modify the returned list
        tasks.append("Fake Task")

        # The internal list should not be affected
        new_tasks = service.get_all_tasks()
        assert len(new_tasks) == original_length


class TestTodoServiceMarkComplete:
    """Test cases for the TodoService mark_complete functionality."""

    def test_mark_complete_existing_task(self):
        """Test marking an existing task as complete."""
        service = TodoService()
        task = service.add_task("Test Task")

        result = service.mark_complete(task.id)

        assert result is True
        assert task.status.name == "COMPLETE"

    def test_mark_complete_nonexistent_task(self):
        """Test marking a non-existent task as complete."""
        service = TodoService()

        result = service.mark_complete(999)

        assert result is False

    def test_mark_complete_already_complete_task(self):
        """Test marking a task that is already complete."""
        service = TodoService()
        task = service.add_task("Test Task")
        service.mark_complete(task.id)  # Mark as complete

        # Try to mark as complete again
        result = service.mark_complete(task.id)

        assert result is True
        assert task.status.name == "COMPLETE"

    def test_mark_complete_with_multiple_tasks(self):
        """Test marking one task as complete among multiple tasks."""
        service = TodoService()
        task1 = service.add_task("First Task")
        task2 = service.add_task("Second Task")
        task3 = service.add_task("Third Task")

        result = service.mark_complete(task2.id)

        assert result is True
        assert task1.status.name == "INCOMPLETE"
        assert task2.status.name == "COMPLETE"
        assert task3.status.name == "INCOMPLETE"


class TestTodoServiceMarkIncomplete:
    """Test cases for the TodoService mark_incomplete functionality."""

    def test_mark_incomplete_existing_task(self):
        """Test marking an existing task as incomplete."""
        service = TodoService()
        task = service.add_task("Test Task")
        service.mark_complete(task.id)  # First mark as complete

        result = service.mark_incomplete(task.id)

        assert result is True
        assert task.status.name == "INCOMPLETE"

    def test_mark_incomplete_nonexistent_task(self):
        """Test marking a non-existent task as incomplete."""
        service = TodoService()

        result = service.mark_incomplete(999)

        assert result is False

    def test_mark_incomplete_already_incomplete_task(self):
        """Test marking a task that is already incomplete."""
        service = TodoService()
        task = service.add_task("Test Task")

        # Task is already incomplete by default
        result = service.mark_incomplete(task.id)

        assert result is True
        assert task.status.name == "INCOMPLETE"

    def test_mark_incomplete_with_multiple_tasks(self):
        """Test marking one task as incomplete among multiple tasks."""
        service = TodoService()
        task1 = service.add_task("First Task")
        task2 = service.add_task("Second Task")
        task3 = service.add_task("Third Task")

        # Mark all as complete first
        service.mark_complete(task1.id)
        service.mark_complete(task2.id)
        service.mark_complete(task3.id)

        # Mark the second as incomplete
        result = service.mark_incomplete(task2.id)

        assert result is True
        assert task1.status.name == "COMPLETE"
        assert task2.status.name == "INCOMPLETE"
        assert task3.status.name == "COMPLETE"


class TestTodoServiceUpdateTask:
    """Test cases for the TodoService update_task functionality."""

    def test_update_task_title_only(self):
        """Test updating only the title of a task."""
        service = TodoService()
        task = service.add_task("Original Title", "Original Description")

        result = service.update_task(task.id, title="New Title")

        assert result is True
        assert task.title == "New Title"
        assert task.description == "Original Description"

    def test_update_task_description_only(self):
        """Test updating only the description of a task."""
        service = TodoService()
        task = service.add_task("Original Title", "Original Description")

        result = service.update_task(task.id, description="New Description")

        assert result is True
        assert task.title == "Original Title"
        assert task.description == "New Description"

    def test_update_task_both_title_and_description(self):
        """Test updating both title and description of a task."""
        service = TodoService()
        task = service.add_task("Original Title", "Original Description")

        result = service.update_task(task.id, title="New Title", description="New Description")

        assert result is True
        assert task.title == "New Title"
        assert task.description == "New Description"

    def test_update_task_nonexistent_task(self):
        """Test updating a non-existent task."""
        service = TodoService()

        result = service.update_task(999, title="New Title")

        assert result is False

    def test_update_task_empty_title_raises_error(self):
        """Test that updating a task with empty title raises ValueError."""
        service = TodoService()
        task = service.add_task("Original Title")

        try:
            service.update_task(task.id, title="")
            assert False, "Expected ValueError was not raised"
        except ValueError as e:
            assert "Title cannot be empty" in str(e)

    def test_update_task_none_title_no_change(self):
        """Test that updating a task with None title doesn't change the title."""
        service = TodoService()
        task = service.add_task("Original Title")
        original_title = task.title

        # This should not raise an error and should not change the title
        result = service.update_task(task.id, title=None)

        assert result is True
        assert task.title == original_title  # Title should remain unchanged

    def test_update_task_whitespace_title_raises_error(self):
        """Test that updating a task with whitespace-only title raises ValueError."""
        service = TodoService()
        task = service.add_task("Original Title")

        try:
            service.update_task(task.id, title="   ")
            assert False, "Expected ValueError was not raised"
        except ValueError as e:
            assert "Title cannot be empty" in str(e)

    def test_update_task_preserves_status(self):
        """Test that updating a task preserves its status."""
        service = TodoService()
        task = service.add_task("Original Title")
        service.mark_complete(task.id)  # Mark as complete

        # Update the task
        result = service.update_task(task.id, title="New Title")

        assert result is True
        assert task.status.name == "COMPLETE"
        assert task.title == "New Title"


class TestTodoServiceDeleteTask:
    """Test cases for the TodoService delete_task functionality."""

    def test_delete_existing_task(self):
        """Test deleting an existing task."""
        service = TodoService()
        task = service.add_task("Test Task")

        result = service.delete_task(task.id)

        assert result is True
        assert len(service.get_all_tasks()) == 0

    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task."""
        service = TodoService()

        result = service.delete_task(999)

        assert result is False
        assert len(service.get_all_tasks()) == 0

    def test_delete_task_from_multiple_tasks(self):
        """Test deleting one task from multiple tasks."""
        service = TodoService()
        task1 = service.add_task("First Task")
        task2 = service.add_task("Second Task")
        task3 = service.add_task("Third Task")

        result = service.delete_task(task2.id)

        assert result is True
        remaining_tasks = service.get_all_tasks()
        assert len(remaining_tasks) == 2
        assert task1 in remaining_tasks
        assert task3 in remaining_tasks
        assert task2 not in remaining_tasks

    def test_delete_task_preserves_other_task_ids(self):
        """Test that deleting a task doesn't affect IDs of other tasks."""
        service = TodoService()
        task1 = service.add_task("First Task")
        task2 = service.add_task("Second Task")
        task3 = service.add_task("Third Task")

        # Verify initial IDs
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

        # Delete the second task
        service.delete_task(task2.id)

        # Verify remaining tasks still have their original IDs
        remaining_tasks = service.get_all_tasks()
        remaining_ids = [task.id for task in remaining_tasks]
        assert 1 in remaining_ids  # task1.id
        assert 3 in remaining_ids  # task3.id
        assert 2 not in remaining_ids  # task2.id should be gone

    def test_delete_all_tasks(self):
        """Test deleting all tasks one by one."""
        service = TodoService()
        task1 = service.add_task("First Task")
        task2 = service.add_task("Second Task")
        task3 = service.add_task("Third Task")

        # Delete all tasks
        result1 = service.delete_task(task1.id)
        result2 = service.delete_task(task2.id)
        result3 = service.delete_task(task3.id)

        assert result1 is True
        assert result2 is True
        assert result3 is True
        assert len(service.get_all_tasks()) == 0