from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import VendorSerializer,Shop_detailSerializer
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from .models import Shop_detail,Vendor 
from geopy.distance import geodesic

# Create your views here.

class Register_vendor(APIView):
    
    def post(self,request):
        serializer = VendorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Succesfully Registered"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class Vendor_login(APIView):

    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        vendor =authenticate(email=email,password=password)
        if vendor:
            refresh = RefreshToken.for_user(vendor)
            return Response({"access": str(refresh.access_token),"refresh":str(refresh),"status":status.HTTP_200_OK})
        else:
            return Response({"errors":"Invalid Credentials","status":status.HTTP_400_BAD_REQUEST})
        
class Shoplist(generics.ListCreateAPIView):
    serializer_class = Shop_detailSerializer
    permission_classes =[IsAuthenticated]
    def get_queryset(self):
        return Shop_detail.objects.filter(owner = self.request.user)
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class shopdetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=Shop_detailSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Shop_detail.objects.filter(owner = self.request.user)
    
class NearByshop(APIView):
    def get(self,request):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        radius = float(request.query_params.get('radius',5))

        if not latitude or not longitude:
            return Response({"error":"Latitude and Longitude are required"})
        
        latitude =float(latitude)
        longitude=float(longitude)

        all_shops =Shop_detail.objects.all()
        nearby_shops = []
        for shop in all_shops:
            shop_location = (shop.latitude,shop.longitude)
            user_location = (latitude,longitude)
            distance = geodesic(user_location,shop_location).km

            if distance<=radius:
                nearby_shops.append({
                    "name":shop.name,
                    "owner":shop.owner.email,
                    "type_of_business":shop.type_of_business, 
                    "latitude":shop.latitude,
                    "longitude":shop.longitude,
                    "distance":round(distance,2),
                })
        return Response(nearby_shops)

