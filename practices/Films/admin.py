from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from .models import ExtendUser,MoviesName
from django.apps import apps
admin.site.register(ExtendUser)
admin.site.register(MoviesName)
app=apps.get_app_config('graphql_auth')

for model_name,model in app.models.items():
    admin .site.register(model)
