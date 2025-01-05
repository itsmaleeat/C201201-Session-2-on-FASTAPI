from fastapi import FastAPI
import uvicorn
# Uncomment and correct the import paths based on your project structure
# from .routers import news, summary
from app.routers import news, summary

app = FastAPI(
    title="AI based News Summary API",
    version="0.2",
    description="This is the API documentation for News Summary generation",
    contact={
        "name": "Maisha Maliat",
        "url": "https://growwithdata.net",
        "email": "mmaliat2025@gmail.com",
    },
    redoc_url="/documentation",
    docs_url="/try-out",
)

app.include_router(news.router)
app.include_router(summary.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Summary API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8501, reload=True)
