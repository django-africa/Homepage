from __future__ import absolute_import

from django.db import models
from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class PostModel(models.Model):
    title = models.CharField(max_length=60);
    content = RichTextUploadingField()
    pub_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=300, verbose_name = "slug", unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(PostModel, self).save(*args, **kwargs)