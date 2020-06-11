import random

operation = ["+","-","*","/"]
number1 = (1,2,3,4,5,6,7,8,9,10)
number2 = (1,2,3,4,5,6,7,8,9,10)
score = 0
game = 0
even = 0
crap = 0

while game == 0:
    difficulty = int(float(input("Choose Your Difficulty By Picking The Number\n1. Easy\n2. Medium \n3. Hard\n")))
    if difficulty == 1:
        for x in range(10):
            operation = operation[:2]
            operationtwo = random.choice(operation)
            num1 = random.choice(number1)
            num2 = random.choice(number2)
            question = int(input("What is the answer to: "+str(num1)+ str(operationtwo)+str(num2)+"?\n"))
            numbers = [num1, num2]
            answer = eval(str(num1) + (operationtwo) + str (num2))
            if question == answer:
                print("Correct!")
                score += 100
                print("Your score has gone up by 100 points!")
            else:
                print("Wrong :(")
            game = 1
    elif difficulty == 2:
        for x in range(10):
            operationtwo = operation[2]
            num1 = random.choice(number1)
            num2 = random.choice(number2)
            question = int(float(input("What is the answer to: "+str(num1)+ str(operationtwo)+str(num2)+"?\n")))
            numbers = [num1, num2]
            answer = eval(str(num1) + (operationtwo) + str (num2))
            if question == answer:
                print("Correct!")
                score += 150
                print("Your score has gone up by 150 points!")
            else:
                print("Wrong :(")
            game = 1
    elif difficulty == 3:
        crap = 0
        while even == 0:
            operationtwo = operation[3]
            num1 = random.choice(number1)
            num2 = random.choice(number2)
            answer = eval(str(num1) + (operationtwo) + str (num2))
            if answer % 2 >0:
                continue
            else:
                while crap < 10:
                    question = int(input("What is the answer to: "+str(num1)+ str(operationtwo)+str(num2)+"?\n"))
                    crap += 1
                    if question == answer:
                        print("Correct!")
                        score += 250
                        print("Your score has gone up by 250 points!")  
                    else:
                        print("Wrong")
                    break
            if crap < 10:
                continue
            elif crap == 10:
                break
                

    print ("your final score is",score)
    game = 1
    play = int(input("Do u want to play again?\n1. Yes\n2. No\n"))
    if play == 1:
        game = 0
    else:
        print("Ok bye then nerd")
