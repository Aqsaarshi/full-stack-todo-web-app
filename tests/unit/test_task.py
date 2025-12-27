"""
Unit tests for the Task model.
"""
import pytest

from src.models.task import Task, TaskStatus


class TestTask:
    """Test cases for the Task model."""
    
    def test_create_task_with_valid_data(self):
        """Test creating a task with valid data."""
        task = Task(task_id=1, title="Test Task", description="Test Description")
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status == TaskStatus.INCOMPLETE
    
    def test_create_task_with_default_status(self):
        """Test that task is created with default 'incomplete' status."""
        task = Task(task_id=1, title="Test Task")
        
        assert task.status == TaskStatus.INCOMPLETE
    
    def test_create_task_with_complete_status(self):
        """Test creating a task with 'complete' status."""
        task = Task(task_id=1, title="Test Task", status=TaskStatus.COMPLETE)
        
        assert task.status == TaskStatus.COMPLETE
    
    def test_create_task_empty_title_raises_error(self):
        """Test that creating a task with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty or None"):
            Task(task_id=1, title="")
    
    def test_create_task_none_title_raises_error(self):
        """Test that creating a task with None title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty or None"):
            Task(task_id=1, title=None)
    
    def test_create_task_whitespace_title_raises_error(self):
        """Test that creating a task with whitespace-only title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty or None"):
            Task(task_id=1, title="   ")
    
    def test_create_task_negative_id_raises_error(self):
        """Test that creating a task with negative ID raises ValueError."""
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            Task(task_id=-1, title="Test Task")
    
    def test_create_task_zero_id_raises_error(self):
        """Test that creating a task with zero ID raises ValueError."""
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            Task(task_id=0, title="Test Task")
    
    def test_create_task_non_integer_id_raises_error(self):
        """Test that creating a task with non-integer ID raises ValueError."""
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            Task(task_id="1", title="Test Task")
    
    def test_task_str_representation(self):
        """Test string representation of a task."""
        task = Task(task_id=1, title="Test Task", status=TaskStatus.INCOMPLETE)
        expected = "[○] 1. Test Task"
        
        assert str(task) == expected
    
    def test_completed_task_str_representation(self):
        """Test string representation of a completed task."""
        task = Task(task_id=1, title="Test Task", status=TaskStatus.COMPLETE)
        expected = "[✓] 1. Test Task"
        
        assert str(task) == expected
    
    def test_task_repr_representation(self):
        """Test detailed string representation of a task."""
        task = Task(task_id=1, title="Test Task", description="Test Description")
        expected = ("Task(id=1, title='Test Task', "
                   "description='Test Description', status=TaskStatus.INCOMPLETE)")
        
        assert repr(task) == expected
    
    def test_task_to_dict(self):
        """Test converting task to dictionary."""
        task = Task(task_id=1, title="Test Task", description="Test Description")
        expected = {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "status": "incomplete"
        }
        
        assert task.to_dict() == expected
    
    def test_task_from_dict(self):
        """Test creating a task from dictionary."""
        data = {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "status": "complete"
        }
        task = Task.from_dict(data)
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status == TaskStatus.COMPLETE