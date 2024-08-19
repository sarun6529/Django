from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('profile/', views.profile, name='profile'),
    path('first/', views.first, name='first'),
    path('first/Second/', views.Second, name='Second'),
    path('first/Third/', views.Third, name='Third'),
    
]