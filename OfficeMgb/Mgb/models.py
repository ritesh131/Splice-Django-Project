from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        default=''
    )
    name = models.CharField(
        max_length=50,
        blank=True,
        default='Unknown'
    )
    phone = models.IntegerField(
        blank=True,
        default=256,
        max_length=256
    )

    def __str__(self):
        return self.user.username