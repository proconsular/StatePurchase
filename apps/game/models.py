from django.db import models

class AgentData(models.Model):
    name = models.CharField(max_length=255)

class TechData(models.Model):
    schools = models.IntegerField()
    curriculum = models.IntegerField()
    roads = models.IntegerField()
    infrastructure = models.IntegerField()
    police_stations = models.IntegerField()
    police_training = models.IntegerField()

class StatData(models.Model):
    education = models.FloatField(default=0)
    traffic = models.FloatField(default=0)
    crime = models.FloatField(default=0)

class StateData(models.Model):
    name = models.CharField(max_length=255)
    tech = models.ForeignKey(TechData, related_name="state", on_delete=models.CASCADE)
    stats = models.ForeignKey(StatData, related_name="state", on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentData, related_name="states", on_delete=models.CASCADE)
