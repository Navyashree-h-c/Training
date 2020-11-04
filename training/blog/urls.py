from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name = "hello_world"),
    path('users', views.users_list, name = "users_list"),
    path('user', views.insert_user, name = "insert_user"),
    path('user/<int:id>', views.user_detail, name = "user_detail"),
    path('blogs', views.blog_list, name = "blog_list"),
    path('blog', views.insert_blog, name = "insert_blog"),

]