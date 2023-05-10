import random

def get_name():
    name_local = input("What is your name: ")
    return name_local

def get_age():
    age_local = int(input("How old are you: "))
    return age_local


# Main routine
name = get_name()   # 1st function
age = get_age()   # 2nd function
if age <= 11:
    print(f"\nHi {name}. You are too young to play this game.")
elif age > 11:
    print(f"\nHi {name}. This quiz is testing your Te Reo Maori skills."
          f"You will receive 10 questions and your score will be recorded"
          f" out of 10. Have fun!")


# Ask 10 questions

print("Question 1")
answer_1 = input("What is the Maori word for 'Family'? ")
if answer_1 == "Whanau".lower():
    print("Correct")
else:
    print("Incorrect")


print("Question 2")
answer_2 = input("What is the Maori word for 'Wha'? ")
if answer_2 == "Four".lower():
    print("Correct")
else:
    print("Incorrect")


print("Question 3")
answer_3 = input("What is the Maori word for 'Waru'? ")
if answer_3 == "Eight".lower():
    print("Correct")
else:
    print("Incorrect")


print("Question 4")
answer_1 = input("What is the Maori word for 'Tekau'? ")
if answer_1 == "Ten".lower():
    print("Correct")
else:
    print("Incorrect")


print("Question 5")
answer_1 = input("What is the Maori word for 'Family'?")
if answer_1 == "Whanau".lower():
    print("Correct")
else:
    print("Incorrect")