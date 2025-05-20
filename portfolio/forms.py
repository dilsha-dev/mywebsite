# forms.py
from django import forms
from .models import Contact

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'id': 'name-field',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'id': 'email-field',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
                'id': 'subject-field',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'rows': 5,
                'id': 'message-field',
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith(('.com', '.org', '.net', '.ae')):
            raise forms.ValidationError("Please enter a valid email address.")
        return email
