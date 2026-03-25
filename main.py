def quiz(sub_name, ques):
    print(f"{sub_name}")
    name = input("Enter your name\n")
    score = 0
    for items in ques:
        print(f"{items['Question']}")
        print(items['options'])
        user_input = input("choice\n").lower().strip()
        if user_input == items['answer']:
            print("correct")
            score += 1
        else:
            print(f"Incorrect....The correct answer was {items['answer'].upper()}")

    print(f"Hey {name}, Your total score in {sub_name} are {score}/{len(ques)}")

math_questions = [
    {"Question": "144 divided by 12", "options": "A = 12\n B = 13\n C = 14\n D = 15\n", "answer": "a"},
    {"Question": "Value of PI", "options": "A = 3.31\n B = 3.24\n C = 3.14\n D = 3.30\n", "answer": "c"},
    {"Question": "Sqaure of 13", "options": "A = 134\n B = 169\n C = 196\n D = 114\n", "answer": "b"}
]    

CS_questions = [
    {"Question": "Brain of Computer", "options": "A = RAM\n B = CPU\n C = ROM\n D = Motherboard\n", "answer": "b"},
    {"Question": "What is WWW", "options": "A = Warehouse\n B = West\n C = Web\n D = Worm\n", "answer": "c"},
    {"Question": "Snake Language", "options": "A = C++\n B = JS\n C = Java\n D = Python\n", "answer": "d"}
]

GK_questions = [
    {"Question": "Eiffel Tower is situated in", "options": "A = Germany\n B = France\n C = China\n D = America\n", "answer": "b"},
    {"Question": "Colors in rainbow", "options": "A = 5\n B = 4\n C = 6\n D = 7\n", "answer": "d"},
    {"Question": "largest ocean on Earth", "options": "A = Atlantic\n B = Pecific\n C = Arctic\n D = indian\n", "answer": "b"}
]

# --------  Main Menu  ----------
menu = {
    "1": ("Mathematics", math_questions),
    "2": ("Computer Science", CS_questions),
    "3": ("General Knowledge", GK_questions)
}
print( "1 - Maths\n",
      "2 - Computer Science\n",
      "3 -  General Knowledge\n")
choice = input("Which Subject...?")

if choice in menu:
    sub_label, ques_set = menu[choice]
    quiz(sub_label, ques_set)
else:
    print("Options not availabe")