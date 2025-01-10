from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.



def api_home(request, *args, **kwargs):
    body = request.body
    print(type(body))
    data = json.loads(body)
    print(request.headers)
    return JsonResponse(data)