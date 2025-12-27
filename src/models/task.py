"""
Task model representing a single todo item.
"""
from enum import Enum
from typing import Optional


class TaskStatus(Enum):
    """Enum representing the status of a task."""
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


class Task:
    """
    Represents a single todo item with attributes: unique ID (integer), 
    title (string), description (string, optional), status (enum: Complete/Incomplete).
    """
    
    def __init__(self, task_id: int, title: str, description: Optional[str] = None, 
                 status: TaskStatus = TaskStatus.INCOMPLETE):
        """
        Initialize a Task instance.
        
        Args:
            task_id: Unique identifier for the task
            title: Title of the task (required, non-empty)
            description: Description of the task (optional)
            status: Status of the task (default: incomplete)
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or None")
        
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        self.id = task_id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.status = status
    
    def __str__(self) -> str:
        """Return string representation of the task."""
        status_str = "✓" if self.status == TaskStatus.COMPLETE else "○"
        return f"[{status_str}] {self.id}. {self.title}"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the task."""
        return (f"Task(id={self.id}, title='{self.title}', "
                f"description='{self.description}', status={self.status})")
    
    def to_dict(self) -> dict:
        """Convert task to dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create a Task instance from a dictionary."""
        status = TaskStatus(data.get("status", "incomplete"))
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            status=status
        )