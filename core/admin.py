from django.contrib import admin
from .models import UserProfile, FileMetadata, FileSharing, AuditLog, Settings

admin.site.register(UserProfile)
admin.site.register(FileMetadata)
admin.site.register(FileSharing)
admin.site.register(AuditLog)
admin.site.register(Settings)
