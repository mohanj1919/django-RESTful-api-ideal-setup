#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .utilities.pagination import CustomPagination
from .models import Product, Campaign

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups', 'password', 'first_name', 'last_name')

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta
#         model = Group
#         fields = ('url', 'name')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        pagination_serializer_class = CustomPagination
        fields = ('name', 'description', 'thumbnail')

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        pagination_serializer_class = CustomPagination
        fields = ('name', 'occation', 'description', 'offer_valid_till')
