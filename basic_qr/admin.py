from django.contrib import admin
from .models import UserProfile,UploadDocument,DeliverSticker
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UploadDocument)

admin.site.register(DeliverSticker)
