
class State:

    @staticmethod
    def render(state):
        output = ""
        for building in state.buildings.all():
            output += State.renderBuilding(building)
        for company in state.companies.all():
            output += State.renderCompany(company)
        return output

    @staticmethod
    def renderBuilding(building):
        output = ""
        output += "<div class='building " + building.type + " building_" + str(building.id) + "' id='" + str(building.id) + "'></div>"
        return output

    @staticmethod
    def renderCompany(company):
        output = ""
        output += "<div class='company company_" + str(company.id) + "' id='" + str(company.id) + "'></div>"
        return output
