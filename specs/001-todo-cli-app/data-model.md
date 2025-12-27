# Data Model: Todo CLI App

## Task Entity

### Attributes
- **id**: Integer (auto-generated, unique, required)
  - Auto-incrementing identifier for each task
  - Starts from 1 and increases with each new task
- **title**: String (required, non-empty)
  - The main description of the task
  - Must not be empty when creating a task
- **description**: String (optional)
  - Additional details about the task
  - Can be empty or null
- **status**: Enum (required, default: "incomplete")
  - Possible values: "incomplete", "complete"
  - Default value when creating a new task is "incomplete"

### Relationships
- No relationships with other entities (standalone entity)

### Validation Rules
- ID must be unique across all tasks
- Title must not be empty or null when creating a task
- Status must be one of the allowed enum values
- ID must be a positive integer

### State Transitions
- Status can transition from "incomplete" to "complete" (via mark-complete operation)
- Status can transition from "complete" to "incomplete" (via mark-incomplete operation)
- Other attributes (id, title, description) can be modified via update operation