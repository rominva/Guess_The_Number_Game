# My GuessNumber Game
import random

print("""\nwelcome to the <<Guess The Number>> game!
      🔴 in this game first, you have to choose two numbers.
      🟢 then, i will choose a random number between your two numbers.
      🟠 and at last, you have to guess which number i chose.
      🟡 if your guess was wrong, i'll give you a hint to correct it.
      🟣 You have 5 chances to guess the wright number. 
         good luck ❤\n""")

f_num = int(input("choose your first number: "))
s_num = int(input("choose your second number: "))

rondom_num = random.randint(f_num, s_num)

guess_num = int(input("now guess the number that i chose: "))

for r in range(5):
    if not f_num <= guess_num <= s_num:
        print(f"No! your Guess shuld be between {f_num} and {s_num}")
        guess_num = int(input("guess again: "))

    elif guess_num == rondom_num:
        print("Yessss! you won🥳 how did you know that?\nare you a genious os sth!?")
        break

    elif guess_num > rondom_num:
        print("The number you chose is GREATER than my number!")
        guess_num = int(input("guess again: "))

    elif guess_num < rondom_num:
        print("The number you chose is SMALLER than my number!")
        guess_num = int(input("guess again: "))

    elif r == 4:
        print("you lost!")
