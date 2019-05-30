from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem


def index(request):
    if (request.method == 'POST'):
        GroceryItem.objects.create(
            grocery_text=request.POST['grocery-item'], create_date=timezone.now(), completed=False)
        return HttpResponseRedirect(reverse('grocery_list_app:index'))
    else:
        in_progress = GroceryItem.objects.filter(completed=False)
        completed = GroceryItem.objects.filter(completed=True)
        return render(request, 'grocery_list_app/index.html', {
            'in_progress': in_progress,
            'completed': completed,
        })


def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.completed = True
    item.complete_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_list_app:index'))


def remove(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list_app:index'))
