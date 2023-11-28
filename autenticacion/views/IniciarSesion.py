
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'Login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            context['form'] = AuthenticationForm(self.request)
        return context

@method_decorator(login_required, name='dispatch')
def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passworod']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Inicio.html')
        else:
            error_message = 'Credenciales Invalidas, intentelo de nuevo.'
            return render(request, 'Login.html', {'error message': error_message})

    else:
        return render(request, 'Login.html')



class CustomLogoutView(LogoutView):
    template_name = 'Login.html'