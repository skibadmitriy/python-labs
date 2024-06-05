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

for employer in employers:
    if(employers[employer]["position"]) == "System Administrator":
        print("{} has postion {}".format(employer, employers[employer]["position"]))

'''
Ivan Ivanov has postion System Administrator
'''
