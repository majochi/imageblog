from django.db import models
from PIL import Image
import os.path
from django.conf import settings

class Site(models.Model):
    title       = models.CharField(max_length=200)
    subtitle    = models.CharField(max_length=200)
    description = models.TextField()
    pub_date    = models.DateTimeField('date published')
    

    def __unicode__(self):
        return self.title

class Article(models.Model):
    site = models.ForeignKey(Site)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

    def __unicode__(self):
        return self.title

class GalImage(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    make_date = models.DateTimeField('date taken')
    base_file = models.ImageField(upload_to=settings.GALIMAGE_ROOT)

    def __unicode__(self):
        return self.name

    def save(self):
        if not self.id and not self.base_file:
            return

        super(GalImage, self).save()

        filename = self.base_file.file.name
        thumb_file = Image.open(filename)
        thumb_file.thumbnail((200, 200), Image.ANTIALIAS)
        thumb_file.save(filename + ".thumb.jpg")


class Gallery(models.Model):
    site = models.ForeignKey(Site)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    galimages = models.ManyToManyField(GalImage)

    def __unicode__(self):
        return self.title


