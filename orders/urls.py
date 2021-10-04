from django.urls import path, re_path
from django.conf.urls import url
from .views import OrderDetail, OrderList, OrderCreate, OrderDelete, OrderUpdate, GoodsCreate

urlpatterns = [
    path("", OrderList.as_view(), name="home"),
    path("order/<slug:slug>/delete", OrderDelete.as_view(), name="order-delete"),
    path("order/<slug:slug>", OrderDetail.as_view(), name="order-detail"),
    path("create-order/", OrderCreate.as_view(), name="order-create"),
    path("goods-order/", GoodsCreate.as_view(), name="goods-create"),
    path("order/<slug:slug>/update", OrderUpdate.as_view(), name="order-update"),
]
