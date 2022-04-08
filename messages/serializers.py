from django.shortcuts import get_object_or_404
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer
from rest_framework import serializers
from .models import Massage

class MessageSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer()
    receiver = CustomUserSerializer()

    class Meta:
        model = Massage
        fields = ['sender', 'receiver', 'message', 'send_timestamp', 'read_timestamp', 'is_read']

    def create(self, validated_data):
        sender_data = validated_data.pop('sender')
        sender = get_object_or_404(CustomUser, id=sender_data['id'])
        receiver_data = validated_data.pop('receiver')
        receiver = get_object_or_404(CustomUser, id=receiver_data['id'])
        message = Massage.objects.create(sender=sender,receiver=receiver, **validated_data)
        return message
