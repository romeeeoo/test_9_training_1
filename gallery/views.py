from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from gallery.forms import PictureForm
from gallery.models import Picture


# Create your views here.
class PicturesView(ListView):
    template_name = "picture/index.html"
    model = Picture
    context_object_name = "pictures"
    ordering = ("-created_at",)


class PictureDetailView(DetailView):
    template_name = "picture/detailed.html"
    model = Picture

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        picture = self.object
        picture_favoured_by = picture.favored_by.all()
        context["picture_favoured_by"] = picture_favoured_by
        return context


class AddNewPicture(CreateView):
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


class UpdatePicture(UpdateView):
    form_class = PictureForm
    model = Picture
    template_name = "picture/update.html"

    def get_success_url(self):
        return reverse("index")








