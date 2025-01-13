from rest_framework import generics



from .models import Product
from .serializers import ProductSerializer


class Product_detail_view(generics.RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product_create_api_view(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer