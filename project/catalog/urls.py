
from django.conf.urls import url, include
from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'products', ProductViewSet, 'product')

urlpatterns = [
    url(r'^', include(router.urls)),
]
