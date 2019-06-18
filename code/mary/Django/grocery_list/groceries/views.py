from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import GroceryItem


def index(request):
    grocery_item_list=GroceryItem.objects.filter(is_complete=False).order_by('-created_date')
    grocery_item_complete=GroceryItem.objects.filter(is_complete=True).order_by('-completed_date')
    context={
        'grocery_item_list': grocery_item_list,
        'grocery_item_complete': grocery_item_complete,
    }
    return render(request, 'groceries/index.html', context)

def add(request):
    item=request.POST['item_text']
    created=timezone.now()
    item=GroceryItem(item_text=item, created_date=created)
    item.save()
    return HttpResponseRedirect(reverse('groceries:index'))    

def completed(request, pk):
    item=get_object_or_404(GroceryItem, pk=pk)
    item.is_complete=True
    item.completed_date=timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('groceries:index'))
    

def delete(request, pk):
    added_item=get_object_or_404(GroceryItem, pk=pk)
    added_item.delete()
    return HttpResponseRedirect(reverse('groceries:index'))



    