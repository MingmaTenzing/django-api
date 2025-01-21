from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

from api.serializers import User_public_serializer

class ProductSerializer(serializers.ModelSerializer):
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    user = User_public_serializer(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    class Meta: 
        model = Product
        fields = ['url','user', 'title', 'content','price', 'sale_price', 'discount_percentage', 'pk',]
        
    def get_url(self,obj):
        request = self.context.get('request')
        if request is None: 
            return None
        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request )
    
    