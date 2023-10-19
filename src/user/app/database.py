from tortoise.contrib.fastapi import register_tortoise
def init(app):
    register_tortoise(
        app,
        db_url="sqlite://database.db",
        modules={'models': ['app.api.v1.models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )   
