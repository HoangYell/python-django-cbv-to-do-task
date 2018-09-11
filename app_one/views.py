from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from app_one.models import Task
# Create your views here.


class TaskList(generic.ListView):
    model = Task
    fields = '__all__'


class CreateTask(generic.CreateView):
    model = Task
    fields = '__all__'


class UpdateTask(generic.UpdateView):
    model = Task
    fields = '__all__'


class DeleteTask(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('app_one:task_list')
