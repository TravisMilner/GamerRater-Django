from django.db import models

class Games(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=255)
    gamer = models.ForeignKey("Gamers", on_delete=models.CASCADE)
    year = models.IntegerField()
    number_of_players = models.IntegerField()
    play_time = models.IntegerField()
    age_recommendation = models.IntegerField()

