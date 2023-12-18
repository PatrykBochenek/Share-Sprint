from django.contrib import admin
from django.urls import path
from core.views import FileList, UserAuditLogs, AllUserAuditLogs, AllUsers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/files/', FileList.as_view(), name='file-list'),
    path('api/audit-logs/<int:user_id>/', UserAuditLogs.as_view(), name='user-audit-logs'),
    path('api/audit-logs/', AllUserAuditLogs.as_view(), name='all-user-audit-logs'),
    path('api/users', AllUsers.as_view(), name="all-users"),
]
