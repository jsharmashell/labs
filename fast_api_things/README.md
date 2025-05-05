# How to Create and Run a FastAPI App

## Steps to Create and Run a FastAPI App

1. **Install FastAPI and Uvicorn**:
    ```bash
    pip install fastapi uvicorn
    ```

2. **Create a FastAPI Application**:
    Create a file named `books.py` and add the following code:
    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/books")
    def get_books():
        return {"books": ["Book 1", "Book 2", "Book 3"]}
    ```

3. **Run the Application**:
    Use Uvicorn to run the app:
    ```bash
    uvicorn books:app --reload
    ```

4. **Access the Application**:
    Open your browser and go to `http://127.0.0.1:8000/books` to see the app running.

5. **Explore the API Documentation**:
    - Swagger UI: `http://127.0.0.1:8000/docs`
    - ReDoc: `http://127.0.0.1:8000/redoc`

## Notes
- Use `--reload` for auto-reloading during development.
- FastAPI automatically generates interactive API documentation.
- Replace `books.py` with your desired filename if needed.
