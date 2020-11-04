from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Blog, User
from django.core import serializers
from django.utils import timezone

def hello_world(request):
    return HttpResponse("Hello, world.")

#static content
def user_list(request):
    data = [
        {'name': 'Kiran', 'email': 'kiran@redintegro.com'},
        {'name': 'Bharath', 'email': 'bharath@gmail.com'}
    ]
    return JsonResponse(data, safe=False)

def user_detail(request, id):
    data = {'name': 'Kamal', 'email': 'kamal@redintegro.com', 'id': id}
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["POST"])
def insert_user(request):
    data = json.loads(request.body.decode('utf-8'))
    return JsonResponse(data, safe=False)

#Dynamic content Crud operations

#Creation
def blog_list(request):
    data = Blog.objects.all()
    response = serializers.serialize("json", data)
    return HttpResponse(response, content_type='application/json')

#Insertion
@csrf_exempt
@require_http_methods(["POST"])
def insert_blog(request):
    data = json.loads(request.body.decode('utf-8'))

    new_blog = Blog(
        name = data['name'],
        posted_by = data['postedBy'],
        posted_on = timezone.now(),
    )

    new_blog.save()
    return JsonResponse(data, safe=False)

#Updation
@csrf_exempt
@require_http_methods(["POST"])
def update_blog(request, id):
    data = json.loads(request.body.decode('utf-8'))

    old_blog = Blog.objects.get(pk=id)
    old_blog.posted_by = data['postedBy']
    old_blog.save()
    return JsonResponse(data, safe=False)

#Deletion
@csrf_exempt
@require_http_methods(["POST"])
def delete_blog(request, id):
    old_blog = Blog.objects.get(pk=id)
    old_blog.delete()
    
    return HttpResponse("Record Deleted")

#For User model
#Creation
def users_list(request):
    data = User.objects.all()
    response = serializers.serialize("json", data)
    return HttpResponse(response, content_type='application/json')

#Insertion
@csrf_exempt
@require_http_methods(["POST"])
def insert_users(request):
    data = json.loads(request.body.decode('utf-8'))

    new_user = User(
        name = data['name'],
        description = data['description'],
        mobile = data['mobile'],
        email = data['email'],
        posted_by = data['postedBy'],
        posted_on = timezone.now(),
    )

    new_user.save()
    return JsonResponse(data, safe=False)

#Updation
@csrf_exempt
@require_http_methods(["POST"])
def update_user(request, id):
    data = json.loads(request.body.decode('utf-8'))

    old_user = User.objects.get(pk=id)
    old_user.description = data['description']
    old_user.save()
    return JsonResponse(data, safe=False)

#Deletion
@csrf_exempt
@require_http_methods(["POST"])
def delete_user(request, id):
    old_user = User.objects.get(pk=id)
    old_user.delete()
    
    return HttpResponse("Record Deleted")

