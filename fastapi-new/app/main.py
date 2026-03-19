from fastapi import FastAPI
from app.routes.functions_loops import router as functions_loops_router


app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}
# app.include_router(list_router)
app.include_router(functions_loops_router)
