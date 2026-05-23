from django.urls import path
from .views import orderlist


urlpatterns = [
    path('',orderlist.as_view() ),
]