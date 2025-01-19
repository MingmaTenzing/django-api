from django.urls import path, include

from .views import products_model_viewset,Product_detail_view, Product_create_api_view, Product_list_view, alt_api_view, Product_update_view, Product_destory_view, product_mixin_view

from rest_framework import routers

# router = routers.DefaultRouter()

# router.register(r'viewset', products_model_viewset)
urlpatterns = [
    # path("", include(router.urls)),
    path("list", Product_list_view.as_view()),
    path("create", Product_create_api_view.as_view()),
    path("mixin/<int:pk>", product_mixin_view.as_view()),
    path("<int:pk>", Product_detail_view.as_view(), name='product-detail'),
    path("<int:pk>/update", Product_update_view.as_view()),
    path("<int:pk>/destroy", Product_destory_view.as_view()),
    path("alt/<int:pk>", alt_api_view),
]