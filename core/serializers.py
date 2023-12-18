from rest_framework import serializers
from .models import FileMetadata as File
from .models import AuditLog
from django.contrib.auth.models import User

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # remove the password and superuser fields from the serializer
    class Meta:
        model = User
        fields = ('id', 'username')
