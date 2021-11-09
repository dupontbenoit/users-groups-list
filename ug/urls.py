from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.UsersAndGroupsView.as_view(), name='index'),
    path('user/<int:pk>', view=views.UserDetailView.as_view(), name='user-detail'),
]
