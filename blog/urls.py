from django.urls import path
from .views import get_blog_details

urlpatterns = [
    path('<int:pk>', get_blog_details)
]
