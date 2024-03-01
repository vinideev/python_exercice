# Module to generate random numbers
import random
import time

OPERATOR = ["+","-","*"]
MAX_OPERAND = 12
MIN_OPERAND = 3
TOTAL_PROBLEMS = 10

def random_operator():
    right = random.randint(MIN_OPERAND,MAX_OPERAND) #Returns an integer number from the specified range.
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATOR) # For returns a randomly element from the specified sequence

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression) #For make more dynamic and don't have to do all if statements
    return expression, answer


wrong = 0
input("|   Press enter to start!   |") #Are you ready?
print("-" * 30)

start_time = time.time() #In this way we can have time stamps


#To count the operations until ten 

for i in range(TOTAL_PROBLEMS):
    expresssion, answer = random_operator()
    while True:
        guess = input("Problems # " + str(i + 1) + ": " + expresssion + " = ")
        if guess == str(answer):
         break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time,2)       

print("-" * 30)
print("Nice work! You finished in", total_time, "seconds")
        

