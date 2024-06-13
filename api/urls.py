from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter() # Create a router object
router.register(r'comments', views.CommentViewSet) # Register the CommentViewSet with the router


urlpatterns = [
    path('', include(router.urls)), 
]