import random
from hangman_art import stages, logo

lives = 7
print(logo)
names_list = ["shreyas", "nikhil", "shravan", "vedant", "nishant", "chetan", "shivam"]
session_name = random.choice(names_list)

display = []
for i in range(len(session_name)):
    display.append("_")

print(display)
print("")
stage_count = -1
while "_" in (display):
    if lives == 0:
        print("you lost.")
        break

    entered_char = input("guess a letter:").lower()

    if entered_char in display:
        print("no duplicate guesses allowed.")

    if entered_char not in session_name:
        lives -= 1
        print(f"wrong guess! you have {lives} lives left.")
        print(stages[stage_count])
        stage_count = stage_count - 1

    for pos in range(len(session_name)):
        lett = session_name[pos]
        if lett == entered_char:
            display[pos] = lett

    print(f"\n{display}\n")
print(f"you guessed it right.\nthe string was {session_name}")
