from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'name', 'email', 'phone', 'date', 'time',
                  'party_size', 'special_req', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']