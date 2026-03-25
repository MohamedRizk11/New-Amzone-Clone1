from django.urls import path
from .views import Producdetail , Productlist

urlpatterns = [
    path('',Productlist.as_view ),
    path('<int:pk>',Producdetail.as_view ),
]