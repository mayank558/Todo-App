from django.shortcuts import render,redirect,get_object_or_404
from todo.models import Todo

def index(request):

    if request.method=='POST':
        todo=Todo()
        new_todo=request.POST['todo']
        if not new_todo:
            return redirect('index')
        todo.todo=new_todo

        todo.save()
        return redirect('index')

    todos=Todo.objects.all()
    return render(request,'index.html',{'todos':todos})

def delete(request, todo_id):

    if request.method=='POST':

        if request.POST.get('delete'):
            todo = get_object_or_404(Todo, pk=todo_id)
            todo.delete()
            return redirect('index')

        if request.POST.get('complete'):
            todo = get_object_or_404(Todo, pk=todo_id)
            todo.is_completed=True
            todo.save()
            return redirect('index')

        if request.POST.get('update'):
           return render(request, 'update.html', {'todo_id':todo_id})


def update(request, todo_id):
    if request.method=='POST':
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.todo=request.POST['todo']
        todo.save()
        return redirect('index')

   


# Create your views here.
