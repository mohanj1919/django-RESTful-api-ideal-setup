
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited
#     """
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited
#     """
#     queryset = Group.objects.all()
#     serializer_class = serializers.GroupSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
