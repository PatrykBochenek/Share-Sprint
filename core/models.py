from django.db import models
from django.contrib.auth.models import User
from core.upload.user_utils import user_directory_path
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics')
    bio = models.TextField()

class FileMetadata(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)  
    file = models.FileField(upload_to=user_directory_path)
    upload_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    size = models.PositiveIntegerField()

class FileSharing(models.Model):
    file = models.ForeignKey(FileMetadata, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(User, related_name='shared_files', on_delete=models.CASCADE)
    permission = models.CharField(max_length=10)  # Example: 'view', 'edit'
    expiry_date = models.DateTimeField(null=True, blank=True)

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.ForeignKey(FileMetadata, null=True, on_delete=models.SET_NULL)

class Settings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    setting_name = models.CharField(max_length=50)
    setting_value = models.CharField(max_length=100)
