from rest_framework import serializers
from .models import Vendor,Shop_detail
from django.contrib.auth.hashers import make_password



class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id','username','email','password']
        extra_kwargs = {'password':{'write_only':True}}


    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)
    
class Shop_detailSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source="owner.name", read_only=True)  
    class Meta:
        model = Shop_detail
        exclude = ['owner']
