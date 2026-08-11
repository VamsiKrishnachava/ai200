# AI200 Project

## Local Setup

### Activate Python environment

Windows PowerShell:

    .\penv\Scripts\Activate.ps1

### Build and run with Docker

Use Docker Compose to build the containers and start the services in detached mode:

    docker compose up -d --build

This command:
- builds the `api` service from the local `Dockerfile`
- starts the `api` service on port `8000`
- starts the `db` service using PostgreSQL

### Verify the API is running

Open the following URL in your browser or use a tool like `curl`:

    http://localhost:8000/api/v1/db-health

A successful response should look like:

    {
      "database": true
    }

### Notes

- If you want to stop the services:

    docker compose down

- If you make changes to the code, rebuild with:

    docker compose up -d --build
