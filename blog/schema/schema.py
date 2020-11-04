import graphene
from blog.schema.blog_schema import Blog, BlogModel

class Query(graphene.ObjectType):
    blogs = graphene.List(Blog)
    blog = graphene.Field(
        Blog,
        id=graphene.Int(required=True),
    )
    
    def resolve_blogs(self, info):
        return BlogModel.objects.all()

    def resolve_blog(self, info, id):
        return BlogModel.objects.get(pk=id)