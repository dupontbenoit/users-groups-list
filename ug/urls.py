from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.UsersAndGroupsView.as_view(), name='index'),
    path('users/<int:pk>', view=views.UserDetailView.as_view(), name='user-detail'),
    path('groups/<int:pk>', view=views.GroupDetailView.as_view(), name='group-detail'),
    path('import', view=views.ImportView.as_view(), name='import'),
]
