from django.db import models

# Create your models here.
class Table(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()

	def __unicode__(self):
		return self.name

class RandomPick(models.Model):
	text = models.TextField()
	table = models.ForeignKey(Table)
	start_value = models.IntegerField()
	end_value = models.IntegerField()
