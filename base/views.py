from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name='tasks'

    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['count'] = context['tasks'].filter(complete=False).count() #할 일의 개수 세는 함수
        context['count_succ'] = context['tasks'].filter(complete=True).count()
        return context

class TaskDetail(DetailView): 
    model = Task
    context_object_name='task'
    template_name = 'base/task.html'

class TaskCreate(CreateView): #'할일 추가' 코드
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView): #기존 할일 수정하기 위한 코드
    model=Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class DeleteView(DeleteView):
    model=Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    