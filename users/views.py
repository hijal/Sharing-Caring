from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreation

class SignUpViewPage(CreateView):
    form_class = CustomUserCreation
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
