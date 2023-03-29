from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from gallery.forms import PictureForm
from gallery.models import Picture


# Create your views here.
class PicturesView(ListView):
    template_name = "picture/index.html"
    model = Picture
    context_object_name = "pictures"
    ordering = ("-created_at",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["user_favorite"] = self.request.user.favorite_pictures.all()
        return context


class PictureDetailView(DetailView):
    template_name = "picture/detailed.html"
    model = Picture

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        picture = self.object
        picture_favoured_by = picture.favored_by.all()
        context["picture_favoured_by"] = picture_favoured_by
        if self.request.user.is_authenticated:
            context["user_favorite"] = self.request.user.favorite_pictures.all()
        return context


class AddNewPicture(LoginRequiredMixin, CreateView):
    template_name = "picture/add.html"
    model = Picture
    form_class = PictureForm

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            image = form.cleaned_data.get("image")
            description = form.cleaned_data.get("description")
            Picture.objects.create(image=image, author=author, description=description)
            return redirect("index")
        return redirect("index")


class UpdatePicture(UserPassesTestMixin, UpdateView):
    form_class = PictureForm
    model = Picture
    template_name = "picture/update.html"

    def get_success_url(self):
        return reverse("detailed", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm("gallery.change_picture")


class DeletePicture(UserPassesTestMixin, DeleteView):
    template_name = "picture/confirm_delete.html"
    model = Picture
    success_url = reverse_lazy("index")

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm("gallery.delete_picture")
