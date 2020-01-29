from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewTodo
from .models import Todo


# Create your views here.
def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks, 'todoform': NewTodo()}
    return render(request=request, template_name='index.html', context=context)


def add_todo(request):
    task = request.POST['task']
    todo_item = Todo(task=task)
    todo_item.save()
    return redirect('index')