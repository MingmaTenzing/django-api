from django.urls import path
from rest_framework.authtoken import views as authviews
from . import views

urlpatterns = [
    path("", views.api_home),
    path('get-token/', authviews.obtain_auth_token)
    # path("raw", views.raw_api)
]