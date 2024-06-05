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

pprint(employers)
pprint(employers[ivan.id])

'''
{1: Employer(Dmitriy, 40, System Engineer),
 2: Employer(Ivan, 32, System Administrator),
 3: Employer(Peter, 25, QA Engineer)}
Employer(Ivan, 32, System Administrator)
'''
