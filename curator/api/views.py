
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .models import Product, Campaign
from .serializers import ProductSerializer, CampaignSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campaigns to be viewed or edited
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    @detail_route(methods=['get'], url_path='custom_action')
    def testMethond():
        return Response({'message': 'test @detail_route'})

class TwoFactorAuthViewSet():
    """
    API for generating QR code for two factor authentication
    """

