from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def todo(request):

    if request.POST.get('text'):
        # using the data of the userinput (within the post request)
        todo_form = TodoForm(request.POST)
        print(request.POST)

        if todo_form.is_valid():
            new_todo = Todo(text=request.POST['text'])
            # validates and saves input to the database
            new_todo.save()

    todo_form = TodoForm()
    todo_list = Todo.objects.order_by('id')

    context = {'todo_category': 'ToDo', 'todo_list': todo_list, 'todo_form': todo_form}

    return context
    #return render(request, 'index.html', context)

def complete_todo(request, id):

    todo = Todo.objects.get(pk=id)
    todo.complete = True
    todo.save()

def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()

