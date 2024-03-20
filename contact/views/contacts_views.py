from django.shortcuts import render
from contact.models import Contact

def index(request):
    contatcts = Contact.objects.all()

    return render(request, 'contact/index.html')