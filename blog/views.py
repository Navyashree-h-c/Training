from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Blog
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