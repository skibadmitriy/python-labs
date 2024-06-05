employers = [
    [ "Skiba", "Dmitriy", "13.09.1981", "System Engineer" ],
    [ "Ivan", "Ivanov", "09.09.1990", "System Administrator" ]
]

def search(surname, list):
    for employer in list:
        if employer[1] == surname:
            return employer
        
result = search("Ivanov", employers)

print("{} {} has position {}".format(result[0], result[1], result[3]))

'''
Ivan Ivanov has position System Administrator
'''
