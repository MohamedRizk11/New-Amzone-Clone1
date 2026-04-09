from django.urls import path
from .views import Producdetail , Productlist, Brandlist

urlpatterns = [
    path('',Productlist.as_view() ),
    path('<slug:slug>',Producdetail.as_view() ),
    path('brands/',Brandlist.as_view() ),
    path('brands/<slug:slug>',Brandlist.as_view() ),
]

