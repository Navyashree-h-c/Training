from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

def hello_world(request):
    return HttpResponse("Hello, world.")

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