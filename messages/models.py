from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Massage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
    massage = models.TextField(max_length=5000)
    send_timestamp = models.DateTimeField(auto_now_add=True)
    read_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.massage

    class Meta:
        ordering = ('send_timestamp',)