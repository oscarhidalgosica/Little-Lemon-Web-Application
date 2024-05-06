from django.contrib import admin
from .models import Menu, Booking

#admin.site.register(Booking)
#admin.site.register(Menu)

@admin.register(Booking)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('first_name','number_of_guests','reservation_date','reservation_slot')
    list_filter = ('reservation_date',)

@admin.register(Menu)
class MenusAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'inventory')
