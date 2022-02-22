from django.contrib.sites import requests
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe

import os


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.IntegerField(default=0,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    languages = models.CharField(max_length=400, blank=True)
    image_path = models.CharField(max_length=100, blank=True)
    image = models.FilePathField(path="projects/images/")
    repo = models.URLField(max_length=200)

    def __str__(self):
        return self.title


    def image_path_exists(self):
        if self.image_path:
            return self.image_path
        return "projects/images/not_found.png"  # fix missing file with filler

    def image_tag(self):
        if os.path.exists(self.image_path):
            return mark_safe(
                '<img src="/static/%s" width="150" height="150" />' % (
                    self.image))

        return mark_safe(
            '<img src="/static/%s" width="150" height="150" />' % self.image)

    image_tag.short_description = 'Image'

    def valid_repo(self):
        lang_data = requests.get(
            "http://api.github.com/repos/" + self.repo.lstrip(
                "https://www.github.com") + "/languages")

        # print(lang_data.json())
        if lang_data.status_code == 404:
            return False

        # Raises exception when not a 2xx response
        lang_data.raise_for_status()

        if lang_data.status_code != 204:
            return True

        return False

    def repo_default(self):
        if self.valid_repo():
            return self.repo

        return "https://github.com/EazyEgan"

    def project_languages(self):
        lang_data = requests.get("http://api.github.com/repos/"
                                 + self.repo.lstrip("https://www.github.com")
                                 + "/languages")
        # print(lang_data.json())
        if lang_data.status_code == 404:
            return 'No data available'
        # Raises exception when not a 2xx response
        lang_data.raise_for_status()
        if lang_data.status_code != 204:
            return ', '.join(list(lang_data.json().keys()))

        return 'No data available'

    def save(self, *args, **kwargs):
        self.repo = self.repo_default()
        self.languages = self.project_languages()
        self.image_path = self.image_path_exists()
        self.image = self.image_path_exists()
        super(Project, self).save(*args, **kwargs)

@receiver(post_save, sender=Project)
def order_listing_update(sender, instance, created, **kwargs):
    if created:
        instance.order = instance.id
        instance.save()