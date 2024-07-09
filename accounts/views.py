from django.shortcuts import render

#djangoning tayyor viewsini qaytaradi
from django.views.generic import CreateView

#djangodagi tayyor urlni qaytaruvchi
from django.urls import reverse_lazy

#djangoda tayyoy userlar uchun view forma
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class SignUpView(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
