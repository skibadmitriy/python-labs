from pprint import pprint

class Employer:
    def __init__(self, id, name, age, position):
        self.id, self.name, self.age, self.position = id, name, age, position
    def __repr__(self):
        return "Employer(%s, %s, %s)" % (self.name, self.age, self.position)

dmitriy = Employer(1, "Dmitriy", "40", "System Engineer")
ivan = Employer(2, "Ivan", "32", "System Administrator")
petr = Employer(3, "Peter", "25", "QA Engineer")

employers = {
    dmitriy.id: dmitriy,
    ivan.id: ivan,
    petr.id: petr
}

def strict_search(age, employers):
    for id in employers:
        if int(employers[id].age) == int(age):
            return id

result = strict_search(40, employers)

pprint(employers[result])
