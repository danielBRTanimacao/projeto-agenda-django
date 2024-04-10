from django.shortcuts import render
from django import forms

from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone'

def create(request):
    if request.method == "POST":
        context = {
            'form': ContactForm(request.POST),
        }
        return render(request, 'contact/create.html', context)
        

    context = {
        'form': ContactForm(),
    }
    return render(request, 'contact/create.html', context)