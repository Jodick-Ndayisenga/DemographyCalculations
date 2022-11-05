print("welcome to the population composition calculation. Please select any percentage rate on your choice to calculate.")

print("to calculate birth rate percentage, input :b")
print("to calculate death rate percentage, input :d")
print("to calculate survivors rate percentage, input :s")

x = True
while x is True:
    var = input()
    print("You have selected:", var)

    if var == "b" or var == "B":
        try:
            print("Awesome, since you selected birth rate percentage, please enter the number corresponding to all living people")
            y = input()
            print("then enter all people who are dead")
            z = input()
            answer = int(y)+int(z)
            print("here you go, the answer to your calculation is",
                  x, "+", y, "=", answer)
        except:
            print(
                'you have entered something that is relevent. Try a new one based on information')

    elif var == "d" or var == "D":
        try:
            print("Awesome, since you selected death rate percentage, please enter the number corresponding to all who were born")

            y = input()
            print("then, now enter the number corresponding to all living people")
            z = input()
            answer = int(y)-int(z)
            print("you're almost there, the answer to your calculation is",
                  y, "-", z, "=", answer)
        except:
            print(
                'you have entered something that is relevent. Try a new one based on information')

    elif var == "s" or var == "S":
        try:
            print("Awesome, since you selected survivor's rate, please enter the number corresponding to all born folks")
            y = input()
            print(
                "alright, you now need to enter the number corresponding to all people who are dead")
            v = input()
            answer = int(y)-int(v)
            print("that's it, the answer to your calculation is",
                  y, "-", v, "=", answer)
        except:
            print(
                'you have entered something that is relevent. Try a new one based on information')

    else:
        print("Fuck you bitch, you were recommended to enter a valid number and yet you denied. what did you expect? try again to type b, B, d,D,s,S as commends and then enter positive integers")
