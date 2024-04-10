from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from contact.models import Contact

def create(request):
    if request.method == "POST":
        print(request.POST.get('first_name'))

    context = {

    }
    return render(request, 'contact/create.html', context)