import json

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView

from accounts.forms import LoginForm, CustomUserCreationForm


class SuccessUrlMixin:
    def get_success_url(self):
        self.next_url = self.request.GET.get('next')
        print("1", self.next_url)
        if not self.next_url:
            self.next_url = self.request.POST.get('next')
            print("2")
        if not self.next_url:
            self.next_url = reverse('index')
            print("3", self.next_url)
        return self.next_url


class LoginView(TemplateView, SuccessUrlMixin):
    template_name = "login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {"form": form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        form = self.form_class(user_data)
        if not form.is_valid():
            print("log-invalid")
            return redirect("login")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect("login")
        login(request, user)
        success_url = self.get_success_url()
        return JsonResponse({"success_url": success_url})


class RegisterView(View, SuccessUrlMixin):
    # template_name = "user_create.html"
    form_class = CustomUserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {"form": form}
        return render(request, "user_create.html", context)

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        form = self.form_class(user_data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            success_url = self.get_success_url()
            return JsonResponse({"success_url": success_url})
        return JsonResponse({"error": "error"})
        # context = {}
        # context["form"] = form
        # return self.render_to_response(context)


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = "user_detail.html"
    context_object_name = "user_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        favorite_pictures = self.object.favorite_pictures.all()
        context["pictures"] = favorite_pictures
        return context


def logout_view(request):
    logout(request)
    return redirect("index")
