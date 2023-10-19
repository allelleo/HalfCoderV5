from .api.v1.controller import controller as auth_v1_controller
from fastapi import FastAPI

app = FastAPI()

app.include_router(auth_v1_controller, prefix="/api/v1/auth")
