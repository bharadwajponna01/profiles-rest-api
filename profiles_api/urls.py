from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register(r'profiles', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    path('', include(router.urls)),
    
]