import uvicorn
from app import api

if __name__ == "__main__":
    api.load_model()
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)