from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import FileMetadata as File
from .models import AuditLog, UserProfile
from .serializers import FileSerializer, AuditLogSerializer, UserSerializer

class FileList(APIView):
    def get(self, request, format=None):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
    
class UserAuditLogs(APIView):
    def get(self, request, user_id, format=None):
        logs = AuditLog.objects.filter(user=user_id)
        serializer = AuditLogSerializer(logs, many=True)
        return Response(serializer.data)
    
class AllUserAuditLogs(APIView):
    def get(self, request, format=None):
        # raise Exception('This is a test exception' + str(request.user.id))
        logs = AuditLog.objects.all()  # replace AuditLog with your actual model
        data = {"logs": list(logs.values())}
        return JsonResponse(data)
    
class AllUsers(APIView):
    def get(self, request, format=None):
    # get the user models (not user profiles) and the files they own
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
