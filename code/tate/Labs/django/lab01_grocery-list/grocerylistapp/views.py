from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader


from .models import GroceryItem
# Create your views here.

def indexView(request):
    grocery_items_list = GroceryItem.objects.order_by('pub_date')
    context = {
        'grocery_items_list': grocery_items_list,
    }
    return render(request, 'grocerylistapp/index.html' , context)

def addItem(request):
    title = request.POST['item_title']
    quantity = request.POST['item_quantity']
    date = timezone.now()

    item = GroceryItem(item_title = title, item_quantity = quantity, pub_date = date )
    item.save()
    return HttpResponseRedirect(reverse('grocerylistapp:indexView'))

def completeItem(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)

    item.completed_date = request.POST['date_completed']
    item.is_complete = True
    item.save()
    return HttpResponseRedirect(reverse('grocerylistapp:indexView'))

def deleteItem(request, pk):
    item = get_object_or_404(GroceryItem,pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocerylistapp:indexView'))
