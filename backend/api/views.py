from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from django.forms.models import model_to_dict
from django.http import HttpResponse
import json

from products.serializers import ProductSerializer
# Create your views here.


@api_view(['POST', 'GET'])
def api_home(request, *args, **kwargs):
    print(request.body)
    serialize = ProductSerializer(data=request.data)
    if serialize.is_valid():
        instance = serialize.save()
        print(instance)
        print(serialize.data)
        return Response(serialize.data)
    
    # instance = Product.objects.all()
    # print(type(instance))
    # data = {}
    
    # if instance: 
    #     data = ProductSerializer(instance, many=True).data
    
    return Response('not working')


    