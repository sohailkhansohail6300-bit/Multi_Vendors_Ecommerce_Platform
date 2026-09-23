from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userprofile(models.Model):
    user_profile_relation=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_image', default='default_profile_image.jpg')
    shop_detail=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_profile_relation.username