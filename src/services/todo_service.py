"""
TodoService handles the business logic for todo operations.
"""
from typing import List, Optional

from src.models.task import Task, TaskStatus


class TodoService:
    """
    Business logic layer for todo operations.
    Handles all CRUD operations and task management.
    """

    def __init__(self):
        """Initialize the TodoService with an empty in-memory storage."""
        self._tasks: List[Task] = []
        self._next_id = 1

    _UNSET_SENTINEL = object()  # Sentinel value to distinguish "not provided" from "None"
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task with a unique ID and mark it as incomplete by default.
        
        Args:
            title: Title of the task (required)
            description: Description of the task (optional)
            
        Returns:
            Task: The newly created task
            
        Raises:
            ValueError: If title is empty
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        
        task = Task(
            task_id=self._next_id,
            title=title,
            description=description,
            status=TaskStatus.INCOMPLETE
        )
        
        self._tasks.append(task)
        self._next_id += 1
        
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            List[Task]: List of all tasks
        """
        return self._tasks.copy()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id: ID of the task to retrieve
            
        Returns:
            Task: The task with the given ID, or None if not found
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None,
                    description: Optional[str] = None) -> bool:
        """
        Update a task's title or description.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            bool: True if task was updated, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip() if description else ""

        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: ID of the task to delete
            
        Returns:
            bool: True if task was deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        self._tasks.remove(task)
        return True
    
    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.
        
        Args:
            task_id: ID of the task to mark as complete
            
        Returns:
            bool: True if task was marked complete, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        task.status = TaskStatus.COMPLETE
        return True
    
    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.
        
        Args:
            task_id: ID of the task to mark as incomplete
            
        Returns:
            bool: True if task was marked incomplete, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        task.status = TaskStatus.INCOMPLETE
        return True
    
    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task.
        
        Returns:
            int: The next available ID
        """
        return self._next_id