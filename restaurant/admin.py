from django.contrib import admin

# Register your models here.
from .models import Menu, Booking

@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('id','title', 'price', 'inventory')

@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = ('id','name', 'no_of_guests', 'booking_date')
