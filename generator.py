import random

random
user_input1 = int(input("Enter the lower bound: "))
user_input2 = int(input("Enter the upper bound: "))

if user_input1 == user_input2:
    print("Choose another bounds!")
elif user_input1 > user_input2:
    print("The lowest bound higher than upper, opps....")
else:
    answer = random.randint(user_input1, user_input2)
    print(answer)
