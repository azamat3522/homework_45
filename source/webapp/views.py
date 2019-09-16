from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import TaskForm
from webapp.models import Article, STATUS_CHOICES


def index_view(request):
    tasks = Article.objects.all()

    return render(request, 'index.html', context={'tasks': tasks})



def task_view(request, pk):
    task = get_object_or_404(Article, pk=pk)

    return render(request, 'task.html', context={
        'task': task
    })


def task_create_view(request):
    if request.method == 'GET':
        form=TaskForm()
        return render(request, 'create.html', context={
            'status_choices': STATUS_CHOICES,
            'form': form
        })
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Article.objects.create(
                description=form.cleaned_data['description'],
                full_description=form.cleaned_data['full_description'],
                status=form.cleaned_data['status'],
                finish_at=form.cleaned_data['finish_at']
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def task_update_view(request, pk):
    task = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={
            'title': task.description,
            'author': task.full_description,
            'text': task.status,
            'category': task.finish_at
        })
        return render(request, 'update.html', context={'form': form, 'task': task})


    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.full_description = form.cleaned_data['full_description']
            task.status = form.cleaned_data['status']
            task.finish_at = form.cleaned_data['finish_at']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task})


def task_delete_view(request, pk):
    task = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={
            'status_choices': STATUS_CHOICES,
            'task': task
        })

    elif request.method == 'POST':
        task.delete()
        return redirect('index')


def task_check_delete(request):
    tasks = Article.objects.all()
    if request.method == 'GET':
        return render(request, 'check_delete.html', context={'tasks': tasks})

    elif request.method == 'POST':
        values = request.POST.getlist('check')
        check_all = request.POST.get('all')
        print(check_all)
        print(tasks)
        print(values)
        # a = Article.objects.all()
        # print(a)
        # if a.filter(id__in=values):
        #     print(values)
        # else:
        #     print('a')
        Article.objects.filter(id__in=values).delete()
        return render(request, 'index.html', context={'tasks': tasks})



