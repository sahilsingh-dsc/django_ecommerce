from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, SliderViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'slider', SliderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
