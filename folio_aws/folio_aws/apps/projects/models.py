from django.db import models

# Create your models here.

from django.db import models
import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
import requests
import os

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    languages = models.CharField(max_length=400, blank = True)
    image_path = models.CharField(max_length=100, blank = True)
    image = models.FilePathField(path="projects/images/")
    repo = models.URLField(max_length=200)

    def __str__(self):
        return self.title

    def image_path_exists(self):
        #if os.path.exists(self.image_path):
        if self.image_path:
            return self.image_path

        else:
            return "projects/images/not_found.png" # fix missing file with filler


    def image_tag(self):
        if os.path.exists(self.image_path):
            return mark_safe('<img src="/static/%s" width="150" height="150" />' % (self.image))

        else:
            return mark_safe('<img src="/static/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'


    def valid_repo(self):
        lang_data = requests.get(
            "http://api.github.com/repos/" + self.repo.lstrip("https://www.github.com") + "/languages")
        #print(lang_data.json())
        if(lang_data.status_code ==404):
            return False
        lang_data.raise_for_status()  # raises exception when not a 2xx response
        if lang_data.status_code != 204:
            return True
        else:
            return False

    def repo_default(self):
        if self.valid_repo():
            return self.repo
        else:
            return "https://github.com/EazyEgan"


    def project_languages(self):
        lang_data = requests.get("http://api.github.com/repos/" + self.repo.lstrip("https://www.github.com")+"/languages")
        # print(lang_data.json())
        if (lang_data.status_code == 404):
            return 'No data available'
        lang_data.raise_for_status()  # raises exception when not a 2xx response
        if lang_data.status_code != 204:
            #self.languages = ', '.join(list(lang_data.json().keys()))
            return ', '.join(list(lang_data.json().keys()))
        else:
            return 'No data available'

    def save(self, *args, **kwargs):
        self.repo = self.repo_default()
        self.languages = self.project_languages()
        self.image_path = self.image_path_exists()
        self.image = self.image_path_exists()
        super(Project, self).save(*args, **kwargs)





"""class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text"""