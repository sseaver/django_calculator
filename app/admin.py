from django.contrib import admin
from app.models import Operations, Profile
# Register your models here.

admin.site.register([Operations, Profile])
