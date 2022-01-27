from django.db import models


class Summary(models.Model):
    heading = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.heading


class NavBarButton(models.Model):
    title = models.CharField(max_length=100)
    page = models.CharField(max_length=100)
    has_dropdown = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class DropDownButton(models.Model):
    navbar_button = models.ForeignKey(NavBarButton, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=100)

    def __str__(self):
        return self.title
