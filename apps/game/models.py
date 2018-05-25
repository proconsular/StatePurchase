from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)

class GameData(models.Model):
    user = models.ForeignKey(User, related_name="games", on_delete=models.CASCADE)

class AgentData(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(GameData, related_name="agents", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="agent", on_delete=models.CASCADE)

class TechData(models.Model):
    schools = models.IntegerField(default=0)
    curriculum = models.IntegerField(default=0)
    roads = models.IntegerField(default=0)
    infrastructure = models.IntegerField(default=0)
    police_stations = models.IntegerField(default=0)
    police_training = models.IntegerField(default=0)

class StatData(models.Model):
    education = models.FloatField(default=0)
    traffic = models.FloatField(default=0)
    crime = models.FloatField(default=0)
    population = models.IntegerField(default=0)
    money = models.FloatField(default=0)

class StateData(models.Model):
    name = models.CharField(max_length=255)
    tech = models.ForeignKey(TechData, related_name="state", on_delete=models.CASCADE)
    stats = models.ForeignKey(StatData, related_name="state", on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentData, related_name="states", on_delete=models.CASCADE)
    game = models.ForeignKey(GameData, related_name="states", on_delete=models.CASCADE)

class LocationData(models.Model):
    x = models.FloatField()
    y = models.FloatField()

# status: 2, Healthy; 1, Rundown; 0, Abandoned
# efficency: 2, Highly Efficent, 1: Efficent, 0: Inefficent
# type: School, Police Station, Road, Company(_Basic, _Midlevel, _Tech)
# cleanliness: 3, Clean; 2, Littered; 1: Dirty; 0: Vandalized
# size: 1-10

class BuildingData(models.Model):
    status = models.IntegerField(default=2)
    efficency = models.IntegerField(default=0)
    type = models.CharField(max_length=255)
    size = models.IntegerField(default=1)
    cleanliness = models.IntegerField(default=3)
    location = models.ForeignKey(LocationData, on_delete=models.CASCADE)
    state = models.ForeignKey(StateData, related_name="buildings", on_delete=models.CASCADE)

class EffectData(models.Model):
    type = models.CharField(max_length=255)
    turns = models.IntegerField(default=2)
    # strength: 1-10
    strength = models.IntegerField(default=1)
    state = models.ForeignKey(StateData, related_name="effects", on_delete=models.CASCADE)

class CompanyData(models.Model):
    tech = models.IntegerField(default=1)
    efficency = models.IntegerField(default=0)
    size = models.IntegerField(default=1)
    location = models.ForeignKey(LocationData, on_delete=models.CASCADE)
    state = models.ForeignKey(StateData, related_name="companies", on_delete=models.CASCADE)
