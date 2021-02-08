from django.db import models

class Images(models.Model):
    gamer = models.ForeignKey("Gamers", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    image =  models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)