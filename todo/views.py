from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


from .models import Todo


def index(request):
    latest_todos = Todo.objects.order_by('-created_at')
    if request.method == "POST":
            todo_form_value =request.POST.dict()['todo']
            todo = Todo(todo_text = todo_form_value)
            todo.save()
            
    #todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo/index.html', {'latest_todos': latest_todos})