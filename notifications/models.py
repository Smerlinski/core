from django.db import models
from accounts.models import CustomUser

# Create your models here.
class MessageNotification(models.Model):
    u = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='msg_notif_user')
