from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView

from accounts.forms import LoginForm, CustomUserCreationForm


# Create your views here.
class LoginView(TemplateView):
    template_name = "login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {"form": form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return redirect("login")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect("login")
        login(request, user)
        return redirect("index")


def logout_view(request):
    logout(request)
    return redirect("index")


class RegisterView(CreateView):
    template_name = "user_create.html"
    form_class = CustomUserCreationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        context = {}
        context["form"] = form
        return self.render_to_response(context)

