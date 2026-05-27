from django.shortcuts import render
from django.views.generic import ListView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import order ,orderdetail,coupon,Cart,Cartdetail



class orderlist(LoginRequiredMixin, ListView):
    model= order
    paginate_by= 10
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)

        return queryset
    



@login_required
def checkout(request):
    cart=Cart.objects.get(user=request.user,status="Inprogress")
    cart_detail=Cartdetail.objects.filter(cart=cart)
    return render(request,'orders/checkout.html',{'cart':cart,'cart_detail':cart_detail})    