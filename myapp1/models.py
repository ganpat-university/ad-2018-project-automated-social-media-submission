from django.db import models


class User(models.Model):
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.email, self.password)


class User_fb(models.Model):
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)


class User_linkedin(models.Model):
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)
