from .models import Cart,Cartdetail


def get_create_cart(request):
    if request.user.is_authenticated:
        cart,create=Cart.objects.get_or_create(user=request.user,status="Inprogress")
        if not create:
            cart_detail=Cartdetail.objects.filter(cart=cart)
            return {'cart_data':cart,'cart_data_detail':cart_detail}
        return {'cart_data':cart}
    else:
        return{}