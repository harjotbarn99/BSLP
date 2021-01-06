from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from PIL import Image
from django.core.files.storage import default_storage

# Create your models here.

class CandidatePhoto(models.Model):
    venture_name = models.CharField(max_length=100, blank=True)
    image_name = models.TextField(blank=True)

class Candidate(models.Model):
    class Categories(models.TextChoices):
        TECHNOLOGY = "Technology", _("Technology")
        GENERAL = "General", _("General")
        SOCIETY = "Social", _("Social")

    name = models.CharField(max_length=100)
    venture = models.CharField(max_length=100)
    category = models.CharField(choices=Categories.choices, max_length=10)
    details = models.TextField(blank=True,default="")
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
        super.save(*args, **kwargs)
        photoLi = CandidatePhoto.objects.filter(venture_name=self.venture)
        if photoLi.count == 0:
            CandidatePhoto.objects.create(venture_name=self.venture,image_name=self.image.name)
            print("got new pic with \nname =",self.image.name,"\n url = ",self.image.url)
        else:
            photo = photoLi[0]
            if photo.name != "user.png":
                ex = default_storage.exists(photo.name)
                print("exists = ",ex)
                print("replacing ",photo.name, " with ",self.image.name)
                print("url = ",self.image.url)
            photo.image_name=self.image.name
