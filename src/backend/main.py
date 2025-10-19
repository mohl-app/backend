from fastapi import FastAPI
from .api.routes import router

app = FastAPI(title="MOHL API")
app.include_router(router)
