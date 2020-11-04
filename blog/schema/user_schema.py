import graphene
from graphene_django.types import DjangoObjectType
from blog.models import User as UserModel

class User(DjangoObjectType):
    class Meta:
        model = UserModel