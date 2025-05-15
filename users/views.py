from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib import messages

from .forms import CustomRegistrationForm
from .models import Profile, Mentor
from .utils import get_crypto_price


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
        context['profile'] = profile
        context['map_html'] = profile.generate_map()
        
        # Check if user is mentor
        try:
            mentor = Mentor.objects.get(profile=profile, is_active=True, approved=True)
            context['is_mentor'] = True
            context['mentor_info'] = mentor
        except Mentor.DoesNotExist:
            context['is_mentor'] = False
            context['mentor_info'] = None

        # Check crypto price if user has set an alert
        if profile.favorite_crypto and profile.target_price and not profile.price_alert_sent:
            current_price = get_crypto_price(profile.favorite_crypto)
            if current_price and current_price >= float(profile.target_price):
                profile.price_alert_sent = True
                profile.save()
                messages.success(
                    self.request,
                    f'🎯 Price Alert! {profile.favorite_crypto} has reached your target price of ${profile.target_price}! '
                    f'Current price: ${current_price:,.2f}'
                )
            
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


class UpdateCryptoAlertView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        favorite_crypto = request.POST.get('favorite_crypto')
        target_price = request.POST.get('target_price')

        if favorite_crypto and target_price:
            profile.favorite_crypto = favorite_crypto
            profile.target_price = target_price
            profile.price_alert_sent = False  # Reset alert status when updating
            profile.save()
            messages.success(request, f'Price alert set for {favorite_crypto} at ${target_price}')
        else:
            messages.error(request, 'Please select a cryptocurrency and enter a target price')

        return redirect('profile')
