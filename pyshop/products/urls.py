from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('contact/', views.Contact, name='contact'),
        path('about/', views.About, name='about'),
        path('signup/', views.signup, name="signup")
]
