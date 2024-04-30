from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Contact

class ContactForm(forms.ModelForm):

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )
    
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                'last_name',
                ValidationError(
                    'O primeiro nome não pode ser igual ao segundo!',
                    code='invalid'
                )
            )

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )
        # )
        return super().clean()
    
    def clean_first_name(self):
        cleaned_data = self.cleaned_data.get('first_name')
        if cleaned_data == 'ABC':
            self.add_error('first_name',ValidationError(
                'Não digita abc misera',
                code='invalid'
            ))
        return cleaned_data

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        required=True,
        min_length=3,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email',ValidationError('Já existe esse email use outro', code='invalid'))

        return email

