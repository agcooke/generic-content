import logging.handlers
import datetime
import os
import sys
import random
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class PageContent(models.Model):
    modified = models.DateTimeField()
    def_content = models.TextField()
    def_title = models.CharField(max_length=255)
    def_description = models.CharField(max_length=255)
    def_heading = models.CharField(max_length=255)
    def_slogan = models.CharField(max_length=255)
    def_url = models.CharField(max_length=255)
    def_content.allow_tags = True
    published = models.BooleanField()
    published.default = False
    slug = models.SlugField(max_length=128, unique=True)
  
            
    class Meta:
        abstract = True
        ordering = ["-modified"]
    def __unicode__(self):
        return self.def_title

class GenericContent(PageContent):
    def get_absolute_url(self):
        return '/'+self.def_url
    def save(self, * args, ** kwargs):
        self.slug = self.def_url
        super(GenericContent, self).save(*args, ** kwargs)