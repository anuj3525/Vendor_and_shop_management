from django.urls import path
from .views import Register_vendor,Vendor_login,shopdetail,Shoplist,NearByshop


urlpatterns = [
    path('register/',Register_vendor.as_view(),name="registration"),
    path('login/',Vendor_login.as_view(),name="login"),
    path('shops/',Shoplist.as_view(),name="shop_list"),
    path('shops/<int:pk>',shopdetail.as_view(),name="shop_detail"),
    path('nearshop/',NearByshop.as_view(),name="near_by_shop"),

]