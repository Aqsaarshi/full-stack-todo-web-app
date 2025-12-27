---

description: "Task list for Todo CLI App implementation"
---

# Tasks: Todo CLI App

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification requests testing for all features, so test tasks are included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/ directory
- [x] T002 Initialize Python 3.13+ project with basic requirements.txt
- [x] T003 [P] Configure linting and formatting tools (flake8, black)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 [P] Create Task model in src/models/task.py based on data model
- [x] T005 [P] Create TodoService in src/services/todo_service.py for business logic
- [x] T006 Create CLI entry point in src/cli/main.py using argparse
- [x] T007 Configure error handling and logging infrastructure in src/lib/utils.py
- [x] T008 Setup in-memory storage mechanism in TodoService

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with title and optional description, assigning unique IDs and defaulting to incomplete status

**Independent Test**: Can be fully tested by running the add task command with title and description and verifying the task appears in the list with a unique ID and incomplete status

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T009 [P] [US1] Unit test for Task model creation in tests/unit/test_task.py
- [x] T010 [P] [US1] Unit test for TodoService add_task functionality in tests/unit/test_todo_service.py
- [x] T011 [P] [US1] Integration test for CLI add command in tests/integration/test_cli.py

### Implementation for User Story 1

- [x] T012 [US1] Implement add_task method in TodoService to create tasks with unique IDs
- [x] T013 [US1] Implement CLI command for adding tasks in src/cli/main.py
- [x] T014 [US1] Add validation for required title field when adding tasks
- [x] T015 [US1] Add error handling for invalid inputs when adding tasks

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to see all tasks with their ID, title, description, and status in a readable format

**Independent Test**: Can be fully tested by adding tasks and then running the view command to verify all tasks are displayed with correct information and status indicators

### Tests for User Story 2 ⚠️

- [x] T016 [P] [US2] Unit test for TodoService get_all_tasks functionality in tests/unit/test_todo_service.py
- [x] T017 [P] [US2] Integration test for CLI view command in tests/integration/test_cli.py

### Implementation for User Story 2

- [x] T018 [US2] Implement get_all_tasks method in TodoService
- [x] T019 [US2] Implement CLI command for viewing tasks in src/cli/main.py
- [x] T020 [US2] Format output to display tasks with ID, title, description, and status clearly

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 5 - Mark Task Complete/Incomplete (Priority: P1)

**Goal**: Enable users to update the status of tasks to reflect whether they're completed or not

**Independent Test**: Can be fully tested by marking a task as complete/incomplete and verifying the status change is reflected when viewing the task list

### Tests for User Story 5 ⚠️

- [x] T021 [P] [US5] Unit test for TodoService mark_complete functionality in tests/unit/test_todo_service.py
- [x] T022 [P] [US5] Unit test for TodoService mark_incomplete functionality in tests/unit/test_todo_service.py
- [x] T023 [P] [US5] Integration test for CLI mark-complete command in tests/integration/test_cli.py
- [x] T024 [P] [US5] Integration test for CLI mark-incomplete command in tests/integration/test_cli.py

### Implementation for User Story 5

- [x] T025 [US5] Implement mark_complete method in TodoService
- [x] T026 [US5] Implement mark_incomplete method in TodoService
- [x] T027 [US5] Implement CLI command for marking tasks as complete in src/cli/main.py
- [x] T028 [US5] Implement CLI command for marking tasks as incomplete in src/cli/main.py
- [x] T029 [US5] Add error handling for invalid task IDs when marking tasks

**Checkpoint**: At this point, User Stories 1, 2 AND 5 should all work independently

---

## Phase 6: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Enable users to modify the title or description of existing tasks using the task ID

**Independent Test**: Can be fully tested by updating a task's title/description and verifying the changes persist when viewing the task again

### Tests for User Story 3 ⚠️

- [x] T030 [P] [US3] Unit test for TodoService update_task functionality in tests/unit/test_todo_service.py
- [x] T031 [P] [US3] Integration test for CLI update command in tests/integration/test_cli.py

### Implementation for User Story 3

- [x] T032 [US3] Implement update_task method in TodoService
- [x] T033 [US3] Implement CLI command for updating tasks in src/cli/main.py
- [x] T034 [US3] Add validation for required fields when updating tasks
- [x] T035 [US3] Add error handling for invalid task IDs when updating tasks

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 5 should all work independently

---

## Phase 7: User Story 4 - Delete Task (Priority: P2)

**Goal**: Enable users to remove tasks from their todo list using the task ID

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the task list

### Tests for User Story 4 ⚠️

- [x] T036 [P] [US4] Unit test for TodoService delete_task functionality in tests/unit/test_todo_service.py
- [x] T037 [P] [US4] Integration test for CLI delete command in tests/integration/test_cli.py

### Implementation for User Story 4

- [x] T038 [US4] Implement delete_task method in TodoService
- [x] T039 [US4] Implement CLI command for deleting tasks in src/cli/main.py
- [x] T040 [US4] Add error handling for invalid task IDs when deleting tasks

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T041 [P] Documentation updates in README.md with setup and usage instructions
- [x] T042 Code cleanup and refactoring across all modules
- [x] T043 Performance optimization to ensure responses under 1 second
- [x] T044 [P] Additional unit tests in tests/unit/ for edge cases
- [x] T045 Error handling hardening across all components
- [x] T046 Run quickstart.md validation to ensure all commands work as documented

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
- [ ] T009 [P] [US1] Unit test for Task model creation in tests/unit/test_task.py
- [ ] T010 [P] [US1] Unit test for TodoService add_task functionality in tests/unit/test_todo_service.py
- [ ] T011 [P] [US1] Integration test for CLI add command in tests/integration/test_cli.py

# Launch all implementation tasks for User Story 1 together:
- [ ] T012 [US1] Implement add_task method in TodoService to create tasks with unique IDs
- [ ] T013 [US1] Implement CLI command for adding tasks in src/cli/main.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 5 → Test independently → Deploy/Demo
5. Add User Story 3 → Test independently → Deploy/Demo
6. Add User Story 4 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 5
   - Developer D: User Story 3
   - Developer E: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence