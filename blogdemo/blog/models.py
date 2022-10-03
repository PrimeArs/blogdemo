from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="images/")

    def __str__(seft):
        return seft.title