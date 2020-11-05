import graphene
from blog.schema.blog_schema import Blog, BlogModel
from blog.schema.user_schema import User, UserModel, CreateUser

class Query(graphene.ObjectType):
    blogs = graphene.List(Blog)
    blog = graphene.Field(
        Blog,
        id=graphene.Int(required=True),
    )

    users = graphene.List(User)
    user = graphene.Field(
        User,
        id=graphene.Int(required=True),
    )
    
    def resolve_blogs(self, info):
        return BlogModel.objects.all()

    def resolve_blog(self, info, id):
        return BlogModel.objects.get(pk=id)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_user(self, info, id):
        return UserModel.objects.get(pk=id)

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()