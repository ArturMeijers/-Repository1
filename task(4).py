import random

# Funkcija, kas ģenerē jautājumus un atbildes
def generate_question():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    question = f"What is {num1} {operation} {num2}?"
    return question, answer

# Funkcija, kas pārbauda, vai lietotāja atbilde ir pareiza
def check_answer(question, answer, user_answer):
    if user_answer == str(answer):
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is {answer}.")
        return False

# Galvenā spēles funkcija
def play_game():
    print("Welcome to the math quiz!")
    num_questions = 3
    num_correct = 0
    for i in range(num_questions):
        question, answer = generate_question()
        user_answer = input(question + " ")
        if check_answer(question, answer, user_answer):
            num_correct += 1
    print(f"You got {num_correct} out of {num_questions} questions correct.")

# Izpilda spēles funkciju
play_game()