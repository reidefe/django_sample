
from django.db.models.expressions import When
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.db import models
from .models import Orders, Goods
from django.urls import reverse_lazy
from typing import List, Dict, Any


class OrderCreate(CreateView):
    model = Orders
    
    template_name = "create.html"
    success_url = reverse_lazy("home")
    fields = ["counter_party", "quantity", "goods"]


class OrderList(ListView):
    model = Orders
    context_object_name = "order_list"
    template_name = "home.html"

   

class GoodsCreate(CreateView):
    model = Goods
    template_name = "goods_create.html"
    success_url = reverse_lazy("home")
    fields = ("name", "description", "price", "manufacturer")


class OrderDelete(DeleteView):
    model = Orders
    template_name = "delete.html"
    success_url = reverse_lazy("home")
    slug_field = "slug"
    slug_url_kwarg = "slug"


class OrderDetail(DetailView):
    model = Orders
    context_object_name = "order_detail"
    template_name = "detail.html"
    slug_url_kwarg = "slug"
    slug_field = "slug"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(OrderDetail, self).get_context_data(**kwargs)
        instance = self.get_object()
        order_pk = context["order_detail"].pk
        context["goods_detail"] = instance.goods
        context["recommended_goods"] = Goods.objects.filter(
            manufacturer__startswith="c"
        )
        return context


class OrderUpdate(UpdateView):
    model = Orders
    fields = "__all__"
    template_name = "update.html"
    success_url = reverse_lazy("home")
