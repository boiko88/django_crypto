from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomRegistrationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'


class CustomRegisterView(CreateView):
    form_class = CustomRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
