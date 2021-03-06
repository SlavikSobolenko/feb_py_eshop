from django.http import HttpResponse
from django.http import Http404

from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .serializers import UserProfileSerializer, DeliveryAddressSerializer
from django.shortcuts import get_object_or_404
from .models import UserProfile, DeliveryAddress
from .filters import UserProfileFilter, DeliveryAddressFilter


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = LimitOffsetPagination
    filter_class = UserProfileFilter


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        obj = get_object_or_404(UserProfile, pk=self.kwargs.get('user_profile_id'))
        return obj


class DeliveryAddressList(generics.ListCreateAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer
    pagination_class = LimitOffsetPagination
    filter_class = DeliveryAddressFilter


class DeliveryAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeliveryAddressSerializer

    def get_object(self):
        obj = get_object_or_404(DeliveryAddress, pk=self.kwargs.get('delivery_address_id'))
        return obj

