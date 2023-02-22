from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Picture(models.Model):
    image = models.ImageField(upload_to="all_pictures")
    author = models.ForeignKey(to=get_user_model(), related_name="pictures", on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    favored_by = models.ManyToManyField(to=get_user_model(), related_name="favorite_pictures", blank=True)


class Comment(models.Model):
    class Meta:
        ordering = ("-datetime_created",)

    text = models.TextField(
        blank=False,
        null=False,
        max_length=200
    )
    picture = models.ForeignKey(
        to="Picture",
        related_name="comments",
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=get_user_model(),
        related_name="comments",
        null=False, blank=False,
        on_delete=models.CASCADE
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )
