from django.db import models
from cms.models import CMSPlugin

class Bug(CMSPlugin):
    video = models.CharField(blank=True, max_length=200)
