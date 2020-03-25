from django.contrib import admin

# Register your models here.
from myapp1.models import User, User_fb, User_linkedin

admin.site.register(User)
admin.site.register(User_fb)
admin.site.register(User_linkedin)
