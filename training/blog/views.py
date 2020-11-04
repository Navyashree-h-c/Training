from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Blog
from django.core import serializers
from django.utils import timezone

def hello_world(request):
    return HttpResponse("Hello, world.")

def users_list(request):
    data = [
        {'name': "navya", 'email': 'navya@gmail.com'},
        {'name': "charlie", 'email': 'charlie@gmail.com'}
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def insert_user(request):
    data = json.loads(request.body.decode('utf-8'))
    return JsonResponse(data, safe=False)

def user_detail(request,id):
    data = {'name': 'navya', 'email': 'navya@gmail.com', 'id': id}
    return JsonResponse(data)

def blog_list(request):
    data = Blog.objects.all()
    response = serializers.serialize("json", data)
    return HttpResponse(response, content_type="application/json")

@csrf_exempt
@require_http_methods(['POST'])
def insert_blog(request):
    data = json.loads(request.body.decode('utf-8'))

    new_blog = Blog(
        name=data['name'],
        posted_by=data['postedBy'],
        posted_on=timezone.now(),
    )

    new_blog.save()

    return JsonResponse(data)

    