from .api.v1.controller import controller as user_v1_controller
from fastapi import FastAPI
app = FastAPI()

app.include_router(user_v1_controller, prefix="/api/v1/user")

from .database import init
init(app)
