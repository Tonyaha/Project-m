from django.urls import path
from project.apps.users import views

urlpatterns = [
    path(r'login/', views.login, name='login'),
]
