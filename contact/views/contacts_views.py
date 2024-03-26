from django.shortcuts import render, get_object_or_404

from contact.models import Contact

def index(request):
    contatcts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contatcts,
        'site_title': 'Contatos - '
    }

    return render(request, 'contact/index.html', context)

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()

    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    site_title = f"{single_contact.first_name} {single_contact.last_name} - "

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(request, 'contact/contact.html', context)