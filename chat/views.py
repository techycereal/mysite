from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import CreateView, TemplateView
from .forms import RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Login(LoginView):
    template_name = 'chat/login.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('index')
    
class Logout(LogoutView):
    next_page = 'login'

class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'chat/register.html'
    success_url = 'index'
    
    def form_valid(self, form):
        # Save the form and get the instance
        self.object = form.save()
        # Prepare JSON response
        data = {
            'id': self.object.pk,
            'username': self.object.username
        }
        return JsonResponse({'success': True, 'data': data}, status=200)

    def form_invalid(self, form):
        # Prepare JSON response with form errors
        errors = {field: error.get_json_data() for field, error in form.errors.items()}
        return JsonResponse({'success': False, 'errors': errors}, status=400)

class Home(TemplateView):
    template_name = 'chat/index.html'

class Room(LoginRequiredMixin, TemplateView):
    template_name = 'chat/room.html'
    login_url = 'login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_name'] = self.kwargs.get('room_name')
        return context
    

class Chat(LoginRequiredMixin, TemplateView):
    template_name = 'chat/chat.html'
    login_url = 'login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_name'] = self.kwargs.get('room_name')
        return context
