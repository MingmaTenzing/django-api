from rest_framework import viewsets, mixins
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'
    

class ProductGenericViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        permission_classes = [permissions.AllowAny]
        lookup_field = 'pk'