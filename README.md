# TODO APP

## Overview
Welcome to the todo app! This repository contains the source code for a Django-based project. Follow the instructions below to set up, run, and contribute to the project.

## Installation
go to base directory of project

### Prepare the Environment
1. **Create a virtual environment:**
    ```bash
    python3.12 -m venv .venv
    ```

2. **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.dev.txt -r requirements.txt
    ```

4. **Set up pre-commit hooks:**
    ```bash
    pre-commit install
    pre-commit run --all  # runs pre-commit
    ```

### Configure the Project
1. Copy the `default.conf` file to `local.conf`:
    ```bash
    cp todoapp/default.conf local.conf
    ```

2. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

3. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Useful URLs

### Django Admin Panel
- `/admin/`

### API Endpoints

The following API endpoints are available for interacting with tasks in the system.

#### Task Endpoints

- **List Tasks**: `GET /api/tasks/`
    - Retrieves a paginated list of tasks.
    - Supports filtering and searching.
    - Example query parameters:
        - `search`: Filter tasks by title or description.
        - `due_date__gt`: Filter tasks with a due date after the specified date.
        - `due_date__gte`: Filter tasks with a due date on or after the specified date.
        - `due_date__lt`: Filter tasks with a due date before the specified date.
        - `due_date__lte`: Filter tasks with a due date on or before the specified date.
        - `created_at__gt`: Filter tasks created after the specified date.
        - `created_at__gte`: Filter tasks created on or after the specified date.
        - `created_at__lt`: Filter tasks created before the specified date.
        - `created_at__lte`: Filter tasks created on or before the specified date.
    - Example request:
        ```bash
        curl -X GET http://<your-domain>/api/tasks/?search=meeting&due_date__gte=2025-01-01
        ```

- **Create Task**: `POST /api/tasks/`
    - Creates a new task.
    - Requires a JSON payload containing task information.
    - Example request:
        ```bash
        curl -X POST http://<your-domain>/api/tasks/ \
        -H "Content-Type: application/json" \
        -d '{"title": "New Task", "description": "Description of the task", "status": "pending", "due_date": "2025-02-01"}'
        ```

- **Retrieve Task**: `GET /api/tasks/{id}/`
    - Retrieves a task by its ID.
    - Example request:
        ```bash
        curl -X GET http://<your-domain>/api/tasks/1/
        ```

- **Update Task (PUT)**: `PUT /api/tasks/{id}/`
    - Fully updates an existing task by its ID.
    - Example request:
        ```bash
        curl -X PUT http://<your-domain>/api/tasks/1/ \
        -H "Content-Type: application/json" \
        -d '{"title": "Updated Task", "description": "Updated description", "status": "completed", "due_date": "2025-02-10"}'
        ```

- **Partially Update Task (PATCH)**: `PATCH /api/tasks/{id}/`
    - Partially updates an existing task by its ID. Only the fields provided in the request body will be updated.
    - Example request:
        ```bash
        curl -X PATCH http://<your-domain>/api/tasks/1/ \
        -H "Content-Type: application/json" \
        -d '{"status": "completed"}'
        ```

    - In this example, only the `status` field of the task will be updated, leaving other fields unchanged.


- **Delete Task**: `DELETE /api/tasks/{id}/`
    - Deletes a task by its ID.
    - Example request:
        ```bash
        curl -X DELETE http://<your-domain>/api/tasks/1/
        ```

#### Documentation
- Swagger API Docs: `/api/docs/`
    - Detailed API documentation can be accessed at `/api/docs/` which provides information on all available endpoints and query parameters.

    
