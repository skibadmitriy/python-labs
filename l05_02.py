employers = {  
    "Dmitriy Skiba": {
        "birthdate": "13.09.1981",
        "position": "System Engineer"
    },
    "Ivan Ivanov": {
        "birthdate": "10.10.1990",
        "position": "System Administrator"
    }
}

def search(position, dict):
    for employer in dict:
        if(employers[employer]["position"]) == position:
            return employer
        
result = search("System Administrator", employers)

print("{} has position {}".format(result, employers[result]["position"]))

'''
Ivan Ivanov has position System Administrator
'''
