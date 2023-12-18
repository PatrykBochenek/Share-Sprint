from django.urls import path
from .. import views

urlpatterns = [
    path('v1/users/', views.ViewAllUsers.as_view(), name='view_all_users'),
]
