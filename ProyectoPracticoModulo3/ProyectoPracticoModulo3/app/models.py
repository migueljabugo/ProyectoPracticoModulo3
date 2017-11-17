"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Game(models.Model):
	name = models.CharField(max_length=50)
	publisher = models.CharField(max_length=20)
	year = models.IntegerField()
	GENRE = (
		(0, "Action"),
		(1, "Adventure"),
		(2, "Strategy"),
		(3, "RPG"),
		(4, "Sport")
		)
	genre = models.IntegerField(choices = GENRE)
	PLATFORM = (
		(0, "PC"),
		(1, "PS4"),
		(2, "XBOXONE")
		)
	platform = models.IntegerField(choices = PLATFORM)
	score = models.IntegerField()
	online = models.BooleanField()
	pegi = models.IntegerField()

