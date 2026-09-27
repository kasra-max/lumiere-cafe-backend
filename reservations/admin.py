from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'time', 'party_size', 'status']
    list_filter = ['status', 'date']
    list_editable = ['status']