from django.contrib import admin
from .models import userprofile
# Register your models here.

@admin.register(userprofile)
class userprofileAdmin(admin.ModelAdmin):
    list_display=['image','shop_detail','created_at']
    list_filter=['created_at']
    search_fields=['shop_detail']
    