import random
print("Choose a number, you have 5 lives. (1-50)")
num = int(input(""))
rand = random.randint(1, 50)
Lives = 5
while num != rand or Lives < 1:
    print("Wrong Guess.")
    Lives = Lives - 1
    if (num - rand) < 25:
        if (num - rand) < 10:
            print("Hot🔥")
        else:
            print("Warm🌡️")
    elif (num - rand) > 30:
        if (num - rand) > 40:
            print("Ice cold🧊")
        else:
            print("Cold🥶")
    print("Lives =",Lives)
    print("Choose a number, you have ",Lives,"lives. (1-50)")
    num = int(input(""))
if num == rand:
    print("You got it correct!")
    print("With",Lives,"remaining lives!")
    print("The random number was",rand)
elif Lives <= 0:
    print("Lives Finished.")
    print("The random number was",rand)