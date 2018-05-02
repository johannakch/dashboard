from django.shortcuts import render, redirect
from apps.weather.views import weather
from apps.todo.views import todo
from apps.todo.views import complete_todo, delete_completed


def index(request):
    # collecting the context dictionaries of all apps and merge them to one
    weather_context = weather(request)
    todo_context = todo(request)

    merged_context = {**weather_context, **todo_context}

    return render(request, 'index.html', merged_context)


def completeTodo(request, id):
    complete_todo(request, id)

    return redirect('index')

def deleteCompleted(request):
    delete_completed(request)

    return redirect('index')