from django.urls import path
from .views import Producdetail , Productlist, Brandlist ,Branddetail

urlpatterns = [
    path('',Productlist.as_view() ),
    path('<slug:slug>',Producdetail.as_view() ),
    path('brands/',Brandlist.as_view() ),
    path('brands/<slug:slug>',Branddetail.as_view() ),
]

