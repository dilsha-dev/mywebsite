
from django.urls import path
from portfolio import views
from .views import index, contact_view, project

urlpatterns = [
    path('', index, name="home"),              # Homepage
    path('contact/', contact_view, name="contact"),  # Contact page
    path('project/', project, name="project"),       # Projects
]
