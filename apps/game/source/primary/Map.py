from .State import State

class Map:
    def __init__(self):
        self.states = []
        self.states.append(State("Washington", 10))
        self.states.append(State("Oregon", 5))
        self.states.append(State("Idaho", 5))
        self.states.append(State("California", 3))
        self.states.append(State("Nevada", 3))
        self.states.append(State("Montana", 3))
        self.states.append(State("Utah", 3))
        self.states.append(State("Arizona", 3))
        self.states.append(State("Wyoming", 3))
        self.states.append(State("Colorado", 3))
        self.states.append(State("New Mexico", 3))
        self.states.append(State("North Dakota", 3))
        self.states.append(State("South Dakota", 3))
        self.states.append(State("Nebraska", 3))
        self.states.append(State("Kansas", 3))
        self.states.append(State("Oklahoma", 3))
        self.states.append(State("Texas", 3))
        self.states.append(State("Minnesota", 3))
        self.states.append(State("Iowa", 3))
        self.states.append(State("Missouri", 3))
        self.states.append(State("Arkansas", 3))
        self.states.append(State("Louisiana", 3))
        self.states.append(State("Wisconsin", 3))
        self.states.append(State("Illinois", 3))
        self.states.append(State("Tennessee", 3))
        self.states.append(State("Mississippi", 3))
        self.states.append(State("Michigan", 3))
        self.states.append(State("Indiana", 3))
        self.states.append(State("Kentucky", 3))
        self.states.append(State("Alabama", 3))
        self.states.append(State("Ohio", 3))
        self.states.append(State("Georgia", 3))
        self.states.append(State("Florida", 3))
        self.states.append(State("New York", 3))
        self.states.append(State("Pennsylvania", 3))
        self.states.append(State("West Virginia", 3))
        self.states.append(State("Virginia", 3))
        self.states.append(State("North Carolina", 3))
        self.states.append(State("South Carolina", 3))
        self.states.append(State("Vermont", 3))
        self.states.append(State("New Hampshire", 3))
        self.states.append(State("Massachusetts", 3))
        self.states.append(State("Connecticut", 3))
        self.states.append(State("Rhode Island", 3))
        self.states.append(State("New Jersey", 3))
        self.states.append(State("Delaware", 3))
        self.states.append(State("Maryland", 3))
        self.states.append(State("Maine", 3))

    def render(self):
        output = ""
        for state in self.states:
            output += self.renderState(state)
        return output

    def renderState(self, state):
        return "<div class='state "+ self.replaceSpaces(state.name.lower()) + "'></div>"

    def replaceSpaces(self, name):
        output = ""
        for c in name:
            if c == " ":
                output += "_"
            else:
                output += c
        return output
