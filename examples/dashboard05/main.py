import uvicorn


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("b9ui.app:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()
