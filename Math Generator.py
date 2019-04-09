
# coding: utf-8

# In[3]:





# This project is from Github,
#https://github.com/brett-davi5/Python---Math-Quiz-Generator
# This is a Free To Use Project
from random import randint
import random

def greeting():
    print("Welcome to the Random Math Quiz!")
    print("We'll be creating a randomly generated series of math questions for you. Let's get started!")

def numberOfQuestions():
    while True:
        try:
            number = int(input("How many questions would you like to generate? (1-1000)"))
            if(number < 1 or number > 1000):
                print("I'm sorry but your number is out of range. Please select a number between 1 and 1000.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please select a number between 1 and 100.")

def numberOfDigits():
    while True:
        try:
            number = int(input("How many digits would you like each number to be? (1-6)"))
            if(number < 1 or number > 6):
                print("I'm sorry but your number is out of range. Please select a number between 1 and 6.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please select a number between 1 and 6s.")

def addition():
    choice = input("Would you like to include addition (+) operations? [Y/N]")
    if choice == "Y" or choice == "N" or choice == "y" or choice == "n":
        if choice == "Y" or choice == "y":
            operators.append("+")
    else:
        print("Please select either Y or N for your answer.")
        addition()

def subtraction():
    choice = input("Would you like to include subtraction (-) operations? [Y/N]")
    if choice == "Y" or choice == "N" or choice == "y" or choice == "n":
        if choice == "Y" or choice == "y":
            operators.append("-")
    else:
        print("Please select either Y or N for your answer.")
        subtraction()

def division():
    choice = input("Would you like to include division (/) operations? [Y/N]")
    if choice == "Y" or choice == "N" or choice == "y" or choice == "n":
        if choice == "Y" or choice == "y":
            operators.append("/")
    else:
        print("Please select either Y or N for your answer.")
        division()

def multiplication():
    choice = input("Would you like to include multiplication (*) operations? [Y/N]")
    if choice == "Y" or choice == "N" or choice == "y" or choice == "n":
        if choice == "Y" or choice == "y":
            operators.append("*")
    else:
        print("Please select either Y or N for your answer.")
        multiplication()


#Amount Generate Section
def createDigit():
    numberOfDigits = digits
    if(numberOfDigits == 1):
        return random.randint(1,9)
    if(numberOfDigits == 2):
        return random.randint(10,99)
    if(numberOfDigits == 3):
        return random.randint(100,999)
    if(numberOfDigits == 4):
        return random.randint(1000,9999)
    if(numberOfDigits == 5):
        return random.randint(10000,99999)
    if(numberOfDigits == 6):
        return random.randint(100000,999999)

#Question Detail Generate
def generateQuestions():
    questionNumbers = numberOfQuestions
    gen_problems = open(r'question.txt', 'w')
    gen_problems_answers = open(r'answer.txt', 'w')
    while questionNumbers > 0:
        digit1 = createDigit()
        digit2 = createDigit()
        operator = random.choice(operators)

        question = (str(digit1) + operator + str(digit2))

        if(operator == "+"):
            questionAnswers = digit1 + digit2
        if(operator == "-"):

            #Regenerate question if the answer is negative
            while digit1<digit2:
                digit1 = createDigit()
                digit2 = createDigit()

            questionAnswers = digit1 - digit2
        if(operator == "*"):
            questionAnswers = digit1 * digit2
        if(operator == "/"):
            valueCheck = digit1 / digit2
            fullIntegerCheck = valueCheck % 10
            if(fullIntegerCheck == 0):
                questionAnswers = valueCheck
            else:
                questionAnswers = int(valueCheck)

        gen_problems.write(str(questionNumbers)+ ".  " + question + " = ____" + "\n")
        gen_problems_answers.write(str(questionNumbers)+ ".  " + question + " = " + str(questionAnswers) +"\n")
        questionNumbers = questionNumbers - 1

def instructions():
    addition()
    subtraction()
    division()
    multiplication()

def mathQuiz():
    global digits
    global numberOfQuestions
    global operators
    operators = []

    print("Answer each of the following questions to determine the layout and setup of your math quiz.")
    numberOfQuestions = numberOfQuestions()
    digits = numberOfDigits()
    instructions()
    print("GENERATING QUESTIONS")
    generateQuestions()

    print("QUESTIONS COMPLETE, it's inside the folder where this program is in")
    #generateAnswers()
    print("ANSWER KEY GENERATED")


# In[4]:

mathQuiz()


# In[ ]:
