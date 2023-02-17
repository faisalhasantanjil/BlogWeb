from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInformation(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    information = models.CharField(
        max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user)


class Blog(models.Model):
    author = models.ForeignKey(
        UserInformation, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100, default='Title', null=False)
    category = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='blogs')

    def __str__(self):
        return self.title


class Comment(models.Model):
    commenter = models.ForeignKey(
        UserInformation, on_delete=models.SET_NULL, blank=True, null=True)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.blog.id) + '-->' + str(self.commenter)
