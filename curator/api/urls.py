
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProductViewSet, CampaignViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, 'product')
router.register(r'campaigns', CampaignViewSet, 'campaign')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth', obtain_auth_token),
]
