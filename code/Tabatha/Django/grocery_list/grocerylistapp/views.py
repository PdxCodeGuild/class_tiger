from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import GroceryItem

# Create your views here.

def groceries(request):
    grocery_list = GroceryItem.objects.filter(is_completed=False).order_by("-date_created")
    grocery_list_completed = GroceryItem.objects.filter(is_completed=True).order_by("-date_created")
    context = {
        "grocery_list":grocery_list,
        "grocery_list_completed":grocery_list_completed
    }
    return render(request, "grocerylistapp/index.html", context)



def add_item(request):
    if request.method == "GET":
            return render(request, "grocerylistapp/")
    elif request.method == "POST":
            GroceryItem.objects.create(item=request.POST['new_item'], date_created=timezone.now())

            return HttpResponseRedirect(reverse("grocerylistapp:list"))

def complete(request, pk):
    completed_item = get_object_or_404(GroceryItem, pk=pk)
    completed_item.is_completed = True
    completed_item.date_completed = timezone.now()
    completed_item.save()

    return HttpResponseRedirect(reverse("grocerylistapp:list"))

def delete(request, pk):
    completed_item = get_object_or_404(GroceryItem, pk=pk)
    completed_item.delete()

    return HttpResponseRedirect(reverse("grocerylistapp:list"))
