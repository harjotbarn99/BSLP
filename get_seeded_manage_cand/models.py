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

    def delete(self,*args, **kwargs ):
        li = CandidatePhoto.objects.filter(venture_name=self.venture)
        super().delete(*args, **kwargs)
        print("delete trigerred ",li.count())
        if li.count() == 1:
            photo = li[0]
            if photo.image_name != "user.png" and default_storage.exists("profile_pics/"+photo.image_name):
                print("deleting ",photo.image_name)
                default_storage.delete("profile_pics/"+photo.image_name)
            print("deleting objext ")
            photo.delete()
        else :
            print("error")
        return 

    def save(self, *args, **kwargs):
        photoLi = CandidatePhoto.objects.filter(venture_name=self.venture)
        print(photoLi.count())
        if photoLi.count() == 0:
            CandidatePhoto.objects.create(venture_name=self.venture,image_name=self.image.name)
            print("got new pic with \nname =",self.image.name,"\nurl = ",self.image.url)
        elif photoLi.count() == 1:
            photo = photoLi[0]
            if photo.image_name != "user.png":
                ex = default_storage.exists("profile_pics/"+photo.image_name)
                print("got existing pic with \nname =",self.image.name,"\nurl = ",self.image.url)
                print("exists = ",ex)
                if ex :
                    print("deleting ",photo.image_name)
                    default_storage.delete("profile_pics/"+photo.image_name)
            print("replacing ",photo.image_name, " with ",self.image.name)
            photo.image_name=self.image.name
            photo.save()
        else:
            print("\n\n------------------error-------------------\n\n")
        return super().save(*args, **kwargs)
