from pprint import pprint
from itertools import product
from utils import compare, int_val
 
STREET_WORDS = {'улица', 'живет'}
BUILDING_WORDS = {'дом'}
APPARTMENT_WORDS = {'кваритра'}
NAME_WORDS = {'имя', 'зовут'}
SURNAME_WORDS = {'фамилия'}
MIDDLE_NAME_WORDS = {'отчество'}
AGE_WORDS = {'старше', 'младше', 'возраст'}
   
class Person:
    def __init__(self, name, surname, middle_name, age, street, building, appartment):
        self.name, self.surname, self.middle_name, self.age, self.street, self.building, self.appatment = name, surname, middle_name, age, street, building, appartment
        self.key = (name, surname, middle_name)
    
    def fuzzy_compare(self, query):
        q = set(query.split())
        score = 0
        for m, f in zip(
            [STREET_WORDS, NAME_WORDS, SURNAME_WORDS, MIDDLE_NAME_WORDS, AGE_WORDS, BUILDING_WORDS, APPARTMENT_WORDS],
            [self.by_street, self.by_name, self.by_surname, self.by_middle_name, self.by_age, self.by_building, self.by_appartment]
        ):
            if m & q:
                score += f(q)
 
        return score > 0.51
 
    def by_street(self, Q):
        Q = Q - STREET_WORDS
        W = set(self.street.split())
        rez = []
        for a,b in product(Q, W):
            rez += [(compare(a,b),a,b)]
 
        return max(rez)[0]
 
    def by_age(self, Q):
        q_age = max([int_val(q) for q in Q])
        if 'старше' in Q:
            return q_age < self.age
        if 'младше' in Q:
            return q_age > self.age
 
        return q_age+5 >= self.age >=q_age-5 

    def by_building(self, Q):
        q_building = max([int_val(q) for q in Q])
        if q_building == self.building:
            return q_building

    def by_appartment(self, Q):
        q_appartment = max([int_val(q) for q in Q])
        if q_appartment == self.appatment:
            return q_appartment

    def by_name(self, Q):
        Q = Q - NAME_WORDS
        W = set(self.name.split())
        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a,b),a,b)]
 
        return max(rez)[0]
    
    def by_surname(self, Q):
        Q = Q - SURNAME_WORDS
        W = set(self.surname.split())
        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a,b),a,b)]
 
        return max(rez)[0]
    
    def by_middle_name(self, Q):
        Q = Q - MIDDLE_NAME_WORDS
        W = set(self.middle_name.split())
        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a,b),a,b)]
 
        return max(rez)[0]
        
    def __eq__(self, obj):
        if type(obj) == Person:
            return 
        elif type(obj) == str:
            return self.fuzzy_compare(obj)
        else:
            return False
     
    def __repr__(self):
        return "Person('%s','%s','%s',%s,'%s',%s,%s)" % (self.name, self.surname, self.middle_name, self.age, self.street, self.building, self.appatment)
    
if __name__ == '__main__':
    lena = Person("Лена", "Ростова", "Ивновна", 19, "Пушкин", 14, 115)
    oleg = Person("Олег", "Иванов", "Иванович", 34, "Ленского", 10, 11)
    olga = Person("Ольга", "Пушкина", "Михайлович", 28, "Онегина", 11, 12)
    nata = Person("Наташа", "Грибоедова", "Алексадровна", 17, "Ростова", 16, 15)
 
    queries = [
            'имя Ольга',
            'возраст 30',
            'старше 20',
            'младше 20',
            'живет на Пушкина',
            'дом 10',
            'квартира 15',
            'фамилия Ростова',
            'отчество Ивановна',
            'зовут нташа',]
 
    people = {
            lena.key: lena,
            oleg.key: oleg,
            olga.key: olga,
            nata.key: nata
    }
 
    for query, person in product(queries, people.values()):
        if person == query:
            print(query, person)
 