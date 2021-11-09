from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,DetailView
from ug.models import User, Group
from ug.services.import_service import CsvImport
from io import StringIO


class UsersAndGroupsView(TemplateView):
    template_name = 'users-and-groups.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['groups'] = Group.objects.all()
        return context


class UserDetailView(DetailView):
    template_name = 'user-detail.html'
    model = User


class GroupDetailView(DetailView):
    template_name = 'group-detail.html'
    model = Group


class ImportView(TemplateView):
    template_name = 'import.html'

    def post(self, request):
        imp = CsvImport()
        data = StringIO(request.POST.get('csv-data'))
        imp.load(data)
        return redirect("index")

