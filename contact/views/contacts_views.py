from django.shortcuts import render
from contact.models import Contact

def index(request):
    contatcts = Contact.objects.all()

    context = {
        'contacts': contatcts,
    }

    return render(request, 'contact/index.html', context)