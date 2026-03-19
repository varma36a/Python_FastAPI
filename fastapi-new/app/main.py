from fastapi import FastAPI
from app.routes.sets import router as sets_router

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# app.include_router(list_router)
app.include_router(sets_router)
