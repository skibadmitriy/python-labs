import random
from itertools import product
from fuzzywuzzy import fuzz


answer_arr = []


def question_compare(question):
    ratio = 0
    answer = None
    for question2 in answer_arr:
        ratio2 = fuzz.ratio(question, question2[0])         
        if ratio2 > ratio:
            ratio = ratio2
            answer = question2[1]
    return question, ratio, answer


while True:
    question = input("Enter your question > ")
    if question == "quit":
        break
    if question_compare(question)[1] < 70:
        answer = random.choice([True, False])
        answer_arr.append([question, answer])
        if answer == True:
            print("yes")
        elif answer == False:
            print("no")
    else:
        if question_compare(question)[2] == True:
            print("yes")
        elif question_compare(question)[2] == False:
            print("no")


print(answer_arr)
