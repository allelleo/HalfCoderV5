from tortoise.fields import (
    IntField, CharField, TextField,
    ForeignKeyField, ManyToManyField, DateField,
    DatetimeField, OneToOneField
)
from tortoise.models import Model

class BaseModel(Model):
    id = IntField(pk=True)

    class Meta:
        abstract = True

class TimesBaseModel(BaseModel):
    time_created = DatetimeField(auto_now_add=True)
    time_updated = DatetimeField(auto_now=True)

    class Meta:
        abstract = True

class RatingBaseModel(TimesBaseModel):
    score = IntField(default=0)

    class Meta:
        abstract = True
    
    async def add_score(self, score):
        pass
    async def update_score(self, score):
        pass
    async def remove_score(self, score):
        pass

class TypeBaseModel(TimesBaseModel):
    title = CharField(max_length=40)

    class Meta:
        abstract = True