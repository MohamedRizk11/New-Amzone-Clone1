from django.urls import path
from .views import Producdetail , Productlist, Brandlist ,Branddetail
from .api import productlistapi , productdetailapi , brandlistapi , branddetailapi
urlpatterns = [
    path('',Productlist.as_view() ),
    path('<slug:slug>',Producdetail.as_view() ),
    path('brands/',Brandlist.as_view() ),
    path('brands/<slug:slug>',Branddetail.as_view() ),

    # api
    path('api/productlist/', productlistapi.as_view()),
    path('api/productlist/<int:pk>', productdetailapi.as_view()),
    path('api/brandlist/', brandlistapi.as_view()),
    path('api/brandlist/<int:pk>', branddetailapi.as_view()),

  
]

