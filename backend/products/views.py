from rest_framework import generics, viewsets, mixins, permissions, authentication
from rest_framework.exceptions import NotFound
from django.http import Http404
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

#GENERIC CLASS BASED VIEWS
class Product_detail_view(generics.RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class Product_list_view(generics.ListAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Product_destory_view(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class Product_update_view(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content: 
            instance.content = instance.title

class Product_create_api_view(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
# MIXIN VIEWS
class product_mixin_view(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get( self,request, *args, **kwargs, ):
        print(args,kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs): 
        print('its post')
        return self.list(request, *args, **kwargs)
    
    
     
    
    
    
    
#FUNCTION BASED VIEWS
@api_view(['GET', 'POST'])
def alt_api_view(request, pk, *args, **kwargs):
    if request.method == 'GET':
        if pk: 
            query_instance = Product.objects.get(pk=pk)
            serializer = ProductSerializer(query_instance, many=False)
            return Response(serializer.data)
        query_instance = Product.objects.all() 
        serializer = ProductSerializer(query_instance, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        if not request.data: 
            return Response('no data provided please provide through body')
        seriliaze_data = ProductSerializer(data=request.data)
        if seriliaze_data.is_valid():
            seriliaze_data.save()
            print(seriliaze_data)
            return Response(seriliaze_data.data)
        return Response("Wrong data format please check docs")



# VIEWSET CLASS  BASED VIEWS
class products_model_viewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    