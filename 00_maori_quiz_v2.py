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
    print(formatter("*", "Correct"))
            print()
else:
    print(formatter("!", "Incorrect"))
            print()


print("Question 2")
answer_2 = input("What is the Maori word for 'Four'? ")
if answer_2 == "Wha".lower():
    print(formatter("*", "Correct"))
    print()
else:
    print(formatter("!", "Incorrect"))
    print()


print("Question 3")
answer_3 = input("What is the Maori word for 'Eight'? ")
if answer_3 == "Waru".lower():
    print(formatter("*", "Correct"))
    print()
else:
    print(formatter("!", "Incorrect"))
    print()


print("Question 4")
answer_4 = input("What is the Maori word for 'Ten'? ")
if answer_4 == "Tekau".lower():
    print(formatter("*", "Correct"))
    print()
else:
    print(formatter("!", "Incorrect"))
    print()


print("Question 5")
answer_5 = input("What is the Maori word for 'May'? ")
if answer_5 == "Haratua".lower():
    print(formatter("*", "Correct"))
    print()
else:
    print(formatter("!", "Incorrect"))
    print()


print("Question 6")
answer_6 = input("What is the Maori word for 'June'? ")
if answer_6 == "Pipiri".lower():
    print(formatter("*", "Correct"))
    print()
else:
    print(formatter("!", "Incorrect"))
    print()


print("Question 7")
answer_7 = input("What is the Maori word for 'September'? ")
if answer_7 == "Hepetema".lower():
    print(formatter("*", "Correct"))
    print()
else:
    print(formatter("!", "Incorrect"))
    print()


print("Question 8")
answer_8 = input("What is the Maori word for 'Monday'? ")
if answer_8 == "Rahina".lower():
    print(formatter("*", "Correct"))
    print()
else:
    print(formatter("!", "Incorrect"))
    print()


print("Question 9")
answer_9 = input("What is the Maori word for 'Wednesday'? ")
if answer_9 == "Raapa".lower():
    print(formatter("*", "Correct"))
    print()
else:
    print(formatter("!", "Incorrect"))
    print()


print("Question 10")
answer_10 = input("What is the Maori word for 'Saturday'? ")
if answer_10 == "Rahoroi".lower():
    print(formatter("*", "Correct"))
    print()
else:
    print(formatter("!", "Incorrect"))
    print()