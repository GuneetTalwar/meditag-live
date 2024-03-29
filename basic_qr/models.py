from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True,help_text="*")
    contact_no = models.CharField(max_length=100, null=True,help_text="*")
    contact_number_in_case_of_emergency = models.CharField(max_length=100, null=True,help_text="*")
    contact_name_in_case_of_emergency = models.CharField(max_length=100,null=True,help_text="*")
    blood_group = models.CharField(max_length=100, null=True,help_text="*")
    height_cms = models.IntegerField(null=True,help_text="*")
    weight_kgs =models.FloatField(null=True,help_text="*")
    allergies = models.TextField(null=True,blank=True)

    emergencies = models.TextField(null=True,blank=True)

    existing_med_conditions = models.TextField(null=True,blank=True)
    ongoing_medication = models.TextField(null=True,blank=True)
    others = models.TextField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    dob = models.DateField(blank=True,null=True)
    address = models.TextField(null=True,blank=True,help_text="(Fill in to claim your free stickers)(Enter Pin Code)")
    path = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
         ordering = ['created_at']
def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class UploadDocument(models.Model):
    user = models.ForeignKey(User,related_name="documents",on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=250,null=True)
    file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

class DeliverSticker(models.Model):
    user_profile = models.OneToOneField(UserProfile,related_name="delivery", on_delete=models.CASCADE, null=True, blank=True)
    complete_address = models.TextField(max_length=200,null=True,help_text="Do not forget to add the pin code")
    path = models.CharField(max_length=200,null=True,blank=True)
