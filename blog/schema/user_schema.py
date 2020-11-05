import graphene
from graphene_django.types import DjangoObjectType
from blog.models import User as UserModel
from django.utils import timezone

class User(DjangoObjectType):
    class Meta:
        model = UserModel


#Mutation Insertion
class CreateUser(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        description = graphene.String()
        mobile = graphene.String()
        email = graphene.String()
        posted_by = graphene.String()

    # The class attributes define the response of the mutation
    user = graphene.Field(User)

    def mutate(self, info, name, description, mobile, email, posted_by):
        new_user = UserModel(
            name = name,
            description = description,
            mobile = mobile,
            email = email,
            posted_by = posted_by,
            posted_on = timezone.now(),
        )

        new_user.save()
        # Notice we return an instance of this mutation
        return CreateUser(user=new_user)

class UpdateUser(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        description = graphene.String()
        posted_by = graphene.String()
        id = graphene.Int()

    # The class attributes define the response of the mutation
    user = graphene.Field(User)

    def mutate(self, info, id, description, posted_by):
        old_user = UserModel.objects.get(pk=id)
        old_user.description = description
        old_user.posted_by = posted_by
        old_user.posted_on = timezone.now()

        old_user.save()
        # Notice we return an instance of this mutation
        return CreateUser(user=old_user)