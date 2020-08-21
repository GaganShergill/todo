from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from . import models, forms
from django.utils import timezone
from django.urls import reverse_lazy
# Create your views here.

class TaskListView(generic.ListView):
    model = models.ToDo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        start = timezone.now().replace(hour=0, minute=0, second=0)
        end = timezone.now().replace(hour=23, minute=59, second=59)
        queryset = models.ToDo.objects.filter(date_created__lte=end, date_created__gte=start, completed=True).count()
        context['taskCompleted'] = queryset
        return context

    def get_queryset(self):
        start = timezone.now().replace(hour=0, minute=0, second=0)
        end = timezone.now().replace(hour=23, minute=59, second=59)
        queryset = models.ToDo.objects.filter(date_created__lte=end, date_created__gte=start).order_by('-date_created')
        return queryset

class TaskCreateView(generic.CreateView):
    redirect_field_name = 'todo/todo_list.html'
    form_class = forms.ToDoForm
    model = models.ToDo

    def form_valid(self, form):
        todo = form.save()
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(generic.UpdateView):
    redirect_field_name = 'todo/todo_list.html'
    form_class = forms.ToDoForm
    model = models.ToDo

class TaskDeleteView(generic.DeleteView):
    model = models.ToDo

    success_url = reverse_lazy('todo:taskList')

def TaskCompleteView(request, pk):
    task = get_object_or_404(models.ToDo, pk=pk)
    task.complete()
    return redirect('todo:taskList')

def TaskNotCompleteView(request, pk):
    task = get_object_or_404(models.ToDo, pk=pk)
    task.notComplete()
    return redirect('todo:taskList')
