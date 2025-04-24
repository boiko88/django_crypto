from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.http import HttpResponse

from .forms import CustomRegistrationForm
from .models import Profile


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'


class CustomRegisterView(CreateView):
    form_class = CustomRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form) -> HttpResponse:
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = Profile.objects.get(user=self.request.user)
        context['map_html'] = profile.generate_map()
        return context

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        new_address = request.POST.get('address')

        if new_address and new_address != profile.address:
            profile.address = new_address
            profile.latitude = None
            profile.longitude = None
            profile.save()

        return redirect('profile')
