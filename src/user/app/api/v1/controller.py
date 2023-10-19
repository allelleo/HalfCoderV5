from fastapi import APIRouter

controller = APIRouter()

@controller.get('/ping')
async def ping():
    return {'message': 'pong'}