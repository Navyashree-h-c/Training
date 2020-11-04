from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('users', views.user_list, name='user_list'),
    path('user/<int:id>', views.user_detail, name='user_detail'),
    path('user', views.insert_user, name='insert_user'),
    path('blogs', views.blog_list, name='blog_list'),
    path('blog', views.insert_blog, name = "insert_blog"),
    path('blog/<int:id>', views.update_blog, name='update_blog'),
    path('blog_delete/<int:id>', views.delete_blog, name='delete_blog'),
]