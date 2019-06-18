from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest,HttpResponse,Http404, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
# from django.template import loader
from django.urls import reverse

#call the models aka tables you need
from .models import GroceryItem
# Create your views here.

def index(request):
    if (request.method == 'POST'):
        # populate these fields with this, "item is the name of the input bos so the value that will be entered"
        name = request.POST['selected_item']
        date = timezone.now()
        #add to my model
        item = GroceryItem(text_description=name, created_date=date, completed=False)
        # redirect here for a response    
        item.save()
        return HttpResponseRedirect(reverse('groceryapp:index'))
    else:
        cart = GroceryItem.objects.filter(completed=False)
        purchase = GroceryItem.objects.filter(completed=True)
        return render(request, 'groceryapp/index.html', {
            'cart': cart,
            'purchase': purchase})


def done(request,pk):
    #get data from db new instance of the row
    grocery_item = get_object_or_404(GroceryItem, pk=pk)
    #each column I need to change for this action
    grocery_item.completed = True
    grocery_item.completed_date = timezone.now()
    #save in the db values of the row
    grocery_item.save()
    #redirectiong the response 
    return HttpResponseRedirect(reverse('groceryapp:index'))

def delete(request,pk):
     #get a new instance of the row by this key
    grocery_item = get_object_or_404(GroceryItem, pk=pk)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('groceryapp:index'))

