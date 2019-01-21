from django.shortcuts import render

from .models import Todo


def index(request):
    latest_todos = Todo.objects.order_by('-created_at')
    if request.method == "POST":
            todo_form_value =request.POST.get('todo')
            todo = Todo(todo_text = todo_form_value)
            todo.save()
            
    return render(request, 'todo/index.html', {'latest_todos': latest_todos})