from .Roll import Roll
from .Map import Map
from .models import *
from random import randint

class Turn:

    @staticmethod
    def process(game):
        for state in game.states.all():
            Turn.processState(state)

    @staticmethod
    def processState(state):
        state.stats.money += Turn.computeIncome(state)
        state.stats.population *= 1.01
        state.stats.traffic = Turn.computeTraffic(state)
        state.stats.crime = Turn.computeCrime(state)
        state.stats.education = Turn.computeEducation(state)
        state.stats.save()
        Turn.breakdown(state)
        Turn.processEffects(state)
        Turn.updateCompanies(state)
        Turn.createCompany(state)
        state.save()

    @staticmethod
    def processEffects(state):
        effects = state.effects.all()
        for effect in effects:
            effect.turns -= 1
            effect.save()
        exhausted_effects = state.effects.filter(turns=0)
        for effect in exhausted_effects:
            effect.delete()

    @staticmethod
    def createCompany(state):
        chance = min(1, state.stats.population / 200) * 0.25 + (1 - Turn.computeCrime(state)) * 0.25 + Turn.computeEducation(state) * 0.5
        if Roll.chance(chance):
             location = LocationData.objects.create(x=randint(10, 800), y=-randint(200, 600))
             location.save()
             com = CompanyData.objects.create(tech=int(Turn.computeEducation(state) * 9 + 1), efficency=int(Turn.computeEducation(state) * 2), size=int(min(10, max(0, state.stats.population / 125))), location_id=location.id, state_id=state.id)
             com.save()

    @staticmethod
    def updateCompanies(state):
        companies = state.companies.all()
        for company in companies:
            if Roll.chance(Turn.computeCrime(state) * 0.5):
                company.delete()

    @staticmethod
    def breakdown(state):
        for building in state.buildings.all():
            if Roll.chance(Turn.computeCrime(state)):
                if building.cleanliness != 0:
                    building.cleanliness -= 1
            stability = min(1 - float(building.cleanliness) / 3.0, 0.9)
            if Roll.chance(stability):
                if building.status != 0:
                    building.status -= 1
            building.save()

    @staticmethod
    def computeIncome(state):
        return Turn.computeGDP(state) * 0.1

    @staticmethod
    def computeGDP(state):
        traffic = 1 - min(Turn.computeTraffic(state), 1)
        crime = state.stats.population * min(Turn.computeCrime(state), 1)
        c_tax = 0.0
        for company in state.companies.all():
            c_tax += (float(company.tech) / 10.0) * (float(company.efficency) / 2.0 + 0.5) * (float(company.size) / 10.0) * 5000.0
        return max(state.stats.population * traffic - crime * 0.5 + c_tax, 0)

    @staticmethod
    def computeTraffic(state):
        roads = state.buildings.filter(type="road")
        capacity = Turn.computeTrafficCapacity(roads)
        if capacity == 0:
            return 1
        base = (state.stats.population * 0.2) / capacity
        return base

    @staticmethod
    def computeTrafficCapacity(roads):
        capacity = 0.0
        for road in roads:
            status = float(road.status) / 2.0
            efficency = float(road.efficency) / 2.0
            size = float(road.size) / 10.0
            capacity += status * (efficency + 0.5) * 300.0 * size
        return capacity

    @staticmethod
    def computeCrime(state):
        stations = state.buildings.filter(type="police")
        capacity = Turn.computeCrimeCapacity(stations)
        if capacity == 0:
            return 1
        base = (state.stats.population * 0.1) / capacity
        crimes = state.effects.filter(type="crime")
        for crime in crimes:
            base += (float(crime.strength) / 10.0) * 0.25
        return base

    @staticmethod
    def computeCrimeCapacity(stations):
        capacity = 0.0
        for station in stations:
            status = float(station.status) / 2.0
            efficency = float(station.efficency) / 2.0
            size = float(station.size) / 10.0
            capacity += status * (efficency + 0.5) * 200.0 * size
        return capacity

    @staticmethod
    def computeEducation(state):
        schools = state.buildings.filter(type="school")
        capacity = Turn.computeSchoolCapacity(schools)
        if capacity == 0:
            return 0
        base = (capacity * 3) / state.stats.population
        return base

    @staticmethod
    def computeSchoolCapacity(stations):
        capacity = 0.0
        for station in stations:
            status = float(station.status) / 2.0
            efficency = float(station.efficency) / 2.0
            size = float(station.size) / 10.0
            capacity += status * (efficency + 0.5) * 20.0 * size
        return capacity
