from django.db import models
from django.utils.timezone import now

# Create your models here.
class Bots:
    name = models.CharField(max_length=200)
    api_key = models.CharField(max_length=200)
    # inject with : in between ex: hello:i am saying hello 
    command_plus_replies = models.CharField(max_length=5000)

class Advertisments(models.Model):
    name = models.CharField(
        max_length=200, help_text="Type Advertisment Title Here")
    content = models.TextField(help_text="Type Or Paste Your Content Here")
    media = models.CharField(
        max_length=300, help_text="Type Or Paste Your Media Link Here", default="")
    publish_date = models.DateField(
        default=now, help_text="The day you want to scheduled this advertisment")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
