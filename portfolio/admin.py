from django.contrib import admin
from .models import Contact  # or ContactMessage if you renamed it

admin.site.register(Contact)  # or ContactMessage
