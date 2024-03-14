# Imports
import random
# Global Variables
correct_answers = 0
question_types = ["+", "-", "x", "/"]

previous_questions = []
previous_user_answers = []
previous_correct_answers = []
# Functions / Methods


def yes_or_no(prompt):
    while True:
        user_choice = input(prompt).upper()
        if user_choice == "YES" or user_choice == "Y":
            return True
        elif user_choice == "NO" or user_choice == "N":
            return False
        else:
            print("ERROR: Please enter Yes or No")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("ERROR: Please enter a valid Number")


def display_question_history():
    global previous_questions, previous_user_answers, previous_correct_answers
    print("\n=== Question History ===\n")
    for i in range(len(previous_questions)):
        output = f"{i + 1}) {previous_questions[i]} | Correct Answer: {previous_correct_answers[i]} | User Answer: {previous_user_answers[i]}"
        print(output)


def one_question():
    global correct_answers, question_types, previous_correct_answers, previous_user_answers, previous_questions
    # Choose 2 random numbers
    first_number = random.randrange(1, 50)
    second_number = random.randrange(1, 50)
    # Chose random question type
    question_type = random.choice(question_types)
    correct_answer = 0

    # Depending on question type add, subtract, multiply or divide numbers and store result in correct_answer.
    if question_type == "+":
        correct_answer = first_number + second_number
    elif question_type == "-":
        correct_answer = first_number - second_number
    elif question_type == "x":
        correct_answer = first_number * second_number
    elif question_type == "/":
        correct_answer = first_number / second_number
        correct_answer = round(correct_answer, 1)
    previous_correct_answers.append(correct_answer)

    # Create question prompt
    question = "What is {} {} {} to one decimal place\n".format(first_number, question_type, second_number)
    previous_questions.append(question)
    # Get User Input
    user_answer = get_number(question)
    user_answer = round(user_answer, 1)
    previous_user_answers.append(user_answer)
    # Check if answer is correct and give score and response based off of result
    if correct_answer == user_answer:
        print("Correct!\n")
        correct_answers += 1
    else:
        print("Incorrect! The correct answer was {}\n".format(correct_answer))


# Main Function
print("==== Math Quiz ====")
print("== By Wal Slavin ==\n")

question_count = 0
while True:
    question_count += 1
    print("Question {}".format(question_count))
    one_question()
    if not yes_or_no("Would you like another question? (Yes/No)\n"):
        break

# Summary of results
print("===Summary===")
print("You got {} / {} questions correct!".format(correct_answers, question_count))
print("{}% of your answers were correct!".format(round((correct_answers / question_count) * 100)))

display_question_history()
input()
