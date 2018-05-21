from .State import State

class Map:
    def __init__(self):
        self.states = []
        self.states.append(State("Washington", 10))
        self.states.append(State("Oregon", 5))
        self.states.append(State("Idaho", 3))

    def render(self):
        output = ""
        for state in self.states:
            output += self.renderState(state)
        return output

    def renderState(self, state):
        return "<div class='state "+ state.name.lower() + "'><div class='handle'></div><img src='static/game/states/images/" + state.name.lower() + ".png'></div>"
