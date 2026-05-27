from django.shortcuts import render
from django.views.generic import ListView 
from .models import order ,orderdetail,coupon,Cart,Cartdetail



class orderlist(ListView):
    model= order
    paginate_by= 10
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)

        return queryset
    



def checkout(request):
    cart=Cart.objects.get(user=request.user,status="Inprogress")
    cart_detail=Cartdetail.objects.filter(cart=cart)
    return render(request,'orders/checkout.html',{'cart':cart,'cart_detail':cart_detail})    