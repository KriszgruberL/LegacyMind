# ⚠️ WORK IN PROGRESS ⚠️

---

# Legacy Bot & AI Brain

This project consists of two components:

- **Legacy Bot**: A Flask-based web service that interacts with the **AI Brain** to send questions and receive responses.
- **AI Brain**: A Flask-based service that uses **LangChain**, **ChromaDB**, and **OpenAI** to generate AI-powered responses.

The **Legacy Bot** serves as the user-facing interface, while the **AI Brain** processes and generates responses to queries.

---

## Project Setup

### Prerequisites

- **Docker**: For containerization of the application.
- **Make** (optional but recommended): To simplify common commands such as starting and stopping the services.
- **Git Bash** or a compatible terminal.

### Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/KriszgruberL/LegacyMind.git
    cd LegacyMind
    ```

2. Build the Docker containers:

    ```bash
    make build
    ```

3. Start the services using Docker Compose:

    ```bash
    make up
    ```

4. Check the health of the services:

    ```bash
    make health
    ```

    This command will check both **legacy-bot** and **ai-brain** services to ensure they are up and running.

---

## Access Swagger UI

Once the services are up and running, you can access the Swagger UI for each service:

- **Legacy Bot**: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)
- **AI Brain**: [http://localhost:8000/apidocs](http://localhost:8000/apidocs)

These Swagger UIs will help you test and interact with the APIs.

---

## Makefile Commands

The following commands are available in the **Makefile** to manage the project:

- **`make up`**: Starts the containers.
- **`make down`**: Stops and removes the containers.
- **`make build`**: Builds the Docker containers.
- **`make rebuild`**: Stops, rebuilds, and restarts the containers.
- **`make logs`**: Follows the logs of both containers.
- **`make restart`**: Stops and restarts the containers.
- **`make ps`**: Lists the containers and their statuses.
- **`make health`**: Checks the health of both services and opens Swagger UI.
- **`make dev`**: Starts both services, runs health checks, and opens Swagger UI automatically.

---

## Folder Structure

- **legacy-bot/**: Contains the Flask application for **Legacy Bot**. This service interacts with the **AI Brain** and presents the user-facing API.
  - `Dockerfile`: Defines the Docker image to run the **Legacy Bot**.
  - `requirements.txt`: Lists dependencies required by **Legacy Bot**.
  - `app.py`: Main application file for the **Legacy Bot** service.


- **ai-brain/**: Contains the Flask application for the **AI Brain**. This service processes and generates responses using **LangChain**, **ChromaDB**, and **OpenAI**.
  - `Dockerfile`: Defines the Docker image to run the **AI Brain**.
  - `requirements.txt`: Lists dependencies required by **AI Brain**.
  - `ai_app.py`: Main application file for the **AI Brain** service.



---

## Dependencies

### Legacy Bot Requirements (`legacy-bot/requirements.txt`):

```plaintext
Flask==1.1.4
gunicorn==19.9.0
requests==2.20.0
unittest2==1.1.0
flasgger==0.9.5
```

### AI Brain Requirements (`ai-brain/requirements.txt`):

```plaintext
flask
langchain
chromadb
openai
flasgger
```

---

## How It Works

### Legacy Bot

- **Legacy Bot** is the interface users interact with. It sends HTTP requests to the **AI Brain** to get responses.
- The **Legacy Bot** accepts **POST** requests, sending a `question` to the **AI Brain**.
- The **Legacy Bot** sends the question to **AI Brain**'s `/ask` API, retrieves the response, and returns it to the user.

### AI Brain

- **AI Brain** processes incoming requests from **Legacy Bot**.
- It uses **LangChain** to chain together large language model calls and other processing components.
- **ChromaDB** is used to store and retrieve vectorized data efficiently, helping with search and retrieval.
- **OpenAI** generates AI-based responses to user queries.

