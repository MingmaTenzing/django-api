from django.urls import path

from .views import Product_detail_view, Product_create_api_view


urlpatterns = [
    path("", Product_create_api_view.as_view()),
    path("<int:pk>", Product_detail_view.as_view())
]