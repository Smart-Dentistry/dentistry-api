from django.urls import path
from api.users.views import UserList

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list')
]
