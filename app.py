from controller import polinomio
from helper import polinomio_helper

still_running = True
user_decision = -1

print("Welcom to operator polynomial")

if True:
    print("Smell")

while(still_running):
    print("Select an option:\n 0: Exit \n 1: Add or Substract two Polynoms\n 2: Product of two Polynoms\n 3: MCD two Polynoms ")
    user_param = input()

    if(user_param.isdigit()): user_decision = int(user_param) 
    else: continue

    if(user_decision >= 0 and user_decision <= 4): still_running = False

if(user_decision == 1): 
    same_lenth = True
    
    print("Enter values, example: 7x^3 + x^2 = 7 2 0 0")

    #while(same_lenth):
    print("First polinom: ")
    x1 = input()
    print("Second polynom: ")
    x2 = input()

    arr = polinomio_helper.validate_arrays(x1, x2)
    result = polinomio.add_polynom(arr)

    print(result)

if(user_decision == 2): 
    same_lenth = True
    
    print("Enter values, example: 7x^3 + x^2 = 7 2 0 0")

    #while(same_lenth):
    print("First polinom: ")
    x1 = input()
    print("Second polynom: ")
    x2 = input()

    arr = polinomio_helper.validate_arrays(x1, x2)
    result = polinomio.product_polynom(arr)

    print(result)