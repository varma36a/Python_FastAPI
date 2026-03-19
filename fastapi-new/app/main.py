from fastapi import FastAPI
#from app.routes.list import router as list_router
from app.routes.tuples import router as tuples_router

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

#app.include_router(list_router)
app.include_router(tuples_router)