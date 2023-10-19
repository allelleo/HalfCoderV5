from tortoise.models import Model
from tortoise.fields import (
    IntField, CharField, TextField,
    ForeignKeyField, ManyToManyField, DateField,
    DatetimeField, OneToOneField, BinaryField
)

from app.abstracts import TimesBaseModel, RatingBaseModel, TypeBaseModel
from app.sugar import override

class UserProfile(TimesBaseModel):
    work = CharField(max_length=100)
    sex = CharField(max_length=3)
    age = IntField(default=-1)
    education = CharField(max_length=100)
    hobby = CharField(max_length=100)
    quote = CharField(max_length=180)
    phone = CharField(max_length=11)
    country = CharField(max_length=100)
    website = CharField(max_length=100)

    class Meta:
        table = 'profile'

class Rating(RatingBaseModel):
    @override
    async def add_score(self, score):
        pass

    @override
    async def update_score(self, score):
        pass

    @override
    async def remove_score(self, score):
        pass

    class Meta:
        table = 'rating'

class RatingPerWeek(RatingBaseModel):
    @override
    async def add_score(self, score):
        pass

    @override
    async def update_score(self, score):
        pass
    
    @override
    async def remove_score(self, score):
        pass

    class Meta:
        table = 'rating_per_week'

class RatingPerMonth(RatingBaseModel):
    @override
    async def add_score(self, score):
        pass

    @override
    async def update_score(self, score):
        pass
    
    @override
    async def remove_score(self, score):
        pass

    class Meta:
        table = 'rating_per_month'

class Politic(TimesBaseModel):
    email = IntField(default=0)
    work = IntField(default=0)
    age = IntField(default=0)
    education = IntField(default=0)
    hobby = IntField(default=0)
    phone = IntField(default=0)
    country = IntField(default=0)
    website = IntField(default=0)

    class Meta:
        table = 'politic'

class BookMarkType(TypeBaseModel):
    class Meta:
        table = 'bookmark_type'

class BookMark(TimesBaseModel):
    to_id = IntField(default=0)
    bookmark_type = ForeignKeyField('models.BookMarkType')
    
    class Meta:
        table = 'bookmark'

class LikeType(TypeBaseModel):
    class Meta:
        table = 'like_type'

class Like(TimesBaseModel):
    to_id = IntField(default=0)
    like_type = ForeignKeyField('models.LikeType')
    
    class Meta:
        table = 'like'

class SubscriptionType(TypeBaseModel):
    class Meta:
        table ='subscription_type'

class Subscription(TimesBaseModel):
    to_id = IntField(default=0)
    subscription_type = ForeignKeyField('models.SubscriptionType')

    class Meta:
        table ='subscription'

class NotificationType(TypeBaseModel):
    class Meta:
        table = 'notification_type'

class Notification(TimesBaseModel):
    title = CharField(max_length=100)
    description = CharField(max_length=100)
    notification_type = ForeignKeyField('models.NotificationType')

    class Meta:
        table = 'notification'

class User(TimesBaseModel):
    username = CharField(max_length=30)
    firstName = CharField(max_length=30)
    lastName = CharField(max_length=30)
    password = BinaryField()
    email = CharField(max_length=30)
    profile = OneToOneField('models.UserProfile')
    rating = OneToOneField('models.Rating')
    ratingWeek = OneToOneField('models.RatingPerWeek')
    ratingMonth = OneToOneField('models.RatingPerMonth')
    politic = OneToOneField('models.Politic')

    bookmarks = ManyToManyField('models.BookMark')
    notifications = ManyToManyField('models.Notification')
    likes = ManyToManyField('models.Like')
    subscribes = ManyToManyField('models.Subscription')