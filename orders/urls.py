from django.urls import path
from .views import orderlist , checkout


urlpatterns = [
    path('',orderlist.as_view() ),
    path('checkout/', checkout),

]