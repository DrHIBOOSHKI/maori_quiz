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