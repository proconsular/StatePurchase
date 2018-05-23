from .models import *

class Map:
    def create(self):
        self.createState("Washington")
        self.createState("Oregon")
        self.createState("Idaho")
        self.createState("California")
        self.createState("Nevada")
        self.createState("Montana")
        self.createState("Utah")
        self.createState("Arizona")
        self.createState("Wyoming")
        self.createState("Colorado")
        self.createState("New Mexico")
        self.createState("North Dakota")
        self.createState("South Dakota")
        self.createState("Nebraska")
        self.createState("Kansas")
        self.createState("Oklahoma")
        self.createState("Texas")
        self.createState("Minnesota")
        self.createState("Iowa")
        self.createState("Missouri")
        self.createState("Arkansas")
        self.createState("Louisiana")
        self.createState("Wisconsin")
        self.createState("Illinois")
        self.createState("Tennessee")
        self.createState("Mississippi")
        self.createState("Michigan")
        self.createState("Indiana")
        self.createState("Kentucky")
        self.createState("Alabama")
        self.createState("Ohio")
        self.createState("Georgia")
        self.createState("Florida")
        self.createState("New York")
        self.createState("Pennsylvania")
        self.createState("West Virginia")
        self.createState("Virginia")
        self.createState("North Carolina")
        self.createState("South Carolina")
        self.createState("Vermont")
        self.createState("New Hampshire")
        self.createState("Massachusetts")
        self.createState("Connecticut")
        self.createState("Rhode Island")
        self.createState("New Jersey")
        self.createState("Delaware")
        self.createState("Maryland")
        self.createState("Maine")

    def createState(self, name):
        tech = TechData.objects.create()
        stats = StatData.objects.create(population=100)
        agent = AgentData.objects.create(name=name, game_id=GameData.objects.first().id)
        tech.save()
        stats.save()
        agent.save()
        state = StateData.objects.create(name=name, tech_id=tech.id, stats_id=stats.id, agent_id=agent.id, game_id=GameData.objects.first().id)
        state.save()

    def render(self):
        output = ""
        states = StateData.objects.filter(game_id=GameData.objects.first().id)
        for state in states:
            output += self.renderState(state)
        return output

    def renderState(self, state):
        name = self.replaceSpaces(state.name.lower())
        return "<a href='/state/" + name + "'><div class='state " + name + "'></div></a>"

    def replaceSpaces(self, name):
        output = ""
        for c in name:
            if c == " ":
                output += "_"
            else:
                output += c
        return output
