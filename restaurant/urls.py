from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

route = DefaultRouter()

route.register(r"table",views.BookingViewSet,basename="table")

urlpatterns = [
    path("",views.index,name="index"),
    path("menu/",views.MenuItemView.as_view(),name="menu"),
    path("menu/<int:pk>",views.SingleMenuItemView.as_view(),name="single_menu"),
    path("booking/",include(route.urls))
] 
