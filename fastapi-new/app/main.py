from fastapi import FastAPI
from app.routes.numpy_pandas import router as numpy_pandas_router


app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}
# app.include_router(list_router)
app.include_router(numpy_pandas_router)
