from django.db import models

# Create your models here.
class VoteCode(models.Model):
    code = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + " - " + self.code
