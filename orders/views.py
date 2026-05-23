from django.shortcuts import render
from django.views.generic import ListView 
from .models import order



class orderlist(ListView):
    model= order

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)

        return queryset