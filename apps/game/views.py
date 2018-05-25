from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .Map import Map
from .models import *
from .Turn import Turn
from .State import State
from .Roll import Roll
from random import randint

def map(request):
    createDeadUser()
    map = startGame(request)
    user = User.objects.filter(username='test')[0]
    request.session['user'] = user.id
    request.session['game'] = user.games.first().id
    context = {
        'map': map.render(),
    }
    return render(request, 'game/map.html', context)

def createDeadUser():
    users = User.objects.filter(username='dead')
    if len(users) == 0:
        User.objects.create(username="dead")

def startGame(request):
    user = None
    game = None
    users = User.objects.filter(username="test")
    if len(users) == 0:
        user = User.objects.create(username="test")
        user.save()
    else:
        user = users[0]
    games = GameData.objects.filter(user_id=user.id)
    if len(games) == 0:
        game = GameData.objects.create(user_id=user.id)
        game.save()
    else:
        game = games[0]
    map = Map()
    states = StateData.objects.filter(game_id=game.id)
    if len(states) == 0:
        map.create()
        WA = StateData.objects.get(name="Washington")
        WA.agent.user = User.objects.get(id=request.session['user'])
        WA.agent.save()

    return map

def state(request, state_name):
    game = GameData.objects.get(id=request.session['game'])
    state = game.states.filter(name__iexact=state_name)[0]
    user_owned = state.agent.user.id == request.session['user']
    context = {
        'state': state,
        'revenue': Turn.computeIncome(state),
        'GDP': Turn.computeGDP(state),
        'rendition': State.render(state),
        'traffic': int(Turn.computeTraffic(state) * 100),
        'crime': int(Turn.computeCrime(state) * 100),
        'education': int(Turn.computeEducation(state) * 100),
        'game': game,
        'user_owned': user_owned,
        'cost': int(state.stats.money + Turn.computeGDP(state))
    }
    return render(request, 'game/state.html', context)

def getBuildingData(request, building_id):
    building = BuildingData.objects.get(id=building_id)
    json = "{\"type\": \""+ building.type +"\", \"status\": \"" + str(building.status) + "\", \"efficency\": \""+ str(building.efficency) + "\", \"size\": \""+ str(building.size) + "\", \"cleanliness\": \""+ str(building.cleanliness) + "\"}"
    return HttpResponse(json)

def getCompanyData(request, company_id):
    building = CompanyData.objects.get(id=company_id)
    json = "{\"tech\": \""+ str(building.tech) +"\", \"efficency\": \"" + str(building.efficency) + "\", \"size\": \""+ str(building.size) + "\"}"
    return HttpResponse(json)

def restart(request):
    GameData.objects.get(id=request.session['game']).delete()
    return redirect('/')

def turn(request):
    game = GameData.objects.get(id=request.session['game'])
    Turn.process(game)
    game.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def fixBuilding(request, building_id):
    building = BuildingData.objects.get(id=building_id)
    state = building.state
    if state.stats.money >= 2.5:
        building.status += 1
        building.save()
        state.stats.money -= 2.5
        state.stats.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def buyBuilding(request, state_id, type):
    state = StateData.objects.get(id=state_id)
    if state.stats.money >= 10:
        location = Map.generateLocation()
        size = 1
        if type == "road":
            size = 1 + state.tech.infrastructure
        elif type == "police":
            size = 1 + state.tech.police_training
        else:
            size = 1 + state.tech.curriculum
        building = BuildingData.objects.create(type=type, efficency=int(Turn.computeEducation(state) * 2), state_id=state.id, location_id=location.id, size=size)
        building.save()
        state.stats.money -= 10
        state.stats.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def improveTech(request, state_id, type):
    state = StateData.objects.get(id=state_id)
    if state.stats.money >= 20:
        if type == "road":
            state.tech.infrastructure += 1
        elif type == "police":
            state.tech.police_training += 1
        elif type == "school":
            state.tech.curriculum += 1
        state.tech.save()
        state.stats.money -= 20
        state.stats.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def clean(request, state_id, type):
    state = StateData.objects.get(id=state_id)
    if state.stats.money >= 5:
        buildings = state.buildings.filter(type=type)
        for building in buildings:
            if building.cleanliness < 3:
                building.cleanliness += 1
            building.save()
        state.stats.money -= 5
        state.stats.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def attack(request, state_id, target_state_id, type):
    state = StateData.objects.get(id=state_id)
    target = StateData.objects.get(id=target_state_id)
    if state.stats.money >= 5:
        if type == "crime":
            strength = randint(1, 5)
            effect = EffectData.objects.create(type=type, strength=strength, state_id=target.id)
            effect.save()
            anti_effect = EffectData.objects.create(type=type, strength=-strength, state_id=state.id)
            anti_effect.save()
        elif type == "road":
            roads = target.buildings.filter(type="road")
            for road in roads:
                if Roll.chance(0.75):
                    if road.cleanliness != 0:
                        road.cleanliness -= 1
                if Roll.chance(0.25):
                    if road.cleanliness != 0:
                        road.cleanliness -= 1
                road.save()
        elif type == "population":
            amount = randint(10, 20)
            state.stats.population += amount
            target.stats.population -= amount
            state.stats.save()
            target.stats.save()
        state.stats.money -= 5
        state.stats.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
