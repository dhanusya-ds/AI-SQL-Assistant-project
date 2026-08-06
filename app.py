from fastapi import FastAPI
from routes.upload import router as upload_router
from routes.query import router as query_router
from routes.learning import router as learning_router

app= FastAPI(
    title="AI SQL Assistant",
    description="Practice SQL using AI",
    version="1.0"
)

app.include_router(upload_router)
app.include_router(query_router)
app.include_router(learning_router)

@app.get("/")
def home():
    return{
        "message":"Welcome to AI SQL Assistant"
    }