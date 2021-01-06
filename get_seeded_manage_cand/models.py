from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from PIL import Image
from django.core.files.storage import default_storage

# Create your models here.


class Candidate(models.Model):
    class Categories(models.TextChoices):
        TECHNOLOGY = "Technology", _("Technology")
        GENERAL = "General", _("General")
        SOCIETY = "Social", _("Social")

    name = models.CharField(max_length=100)
    venture = models.CharField(max_length=100)
    category = models.CharField(choices=Categories.choices, max_length=10)
    details = models.TextField(blank=True, null=True)
    votes = models.SmallIntegerField(default=0)
    image = models.ImageField(default="user.png", upload_to="profile_pics")

    def __str__(self):
        return self.venture

    def get_absolute_url(self):
        return reverse("candidateDetail-GSMC", kwargs={"pk": self.id})

    def castVote(self):
        self.votes += 1
        self.save()
        return

    def save(self, *args, **kwargs):
        name = self.image.name
        super().save(*args, **kwargs)
        if (name != "user.png"):
            default_storage.delete('profile_pics/my-pic.jpg')

