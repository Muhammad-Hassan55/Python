import random
number = random.randint(1,100)
attampts = 12
while attampts > 0 :
    guess = int(input("Guess the  number : "))
    attampts -= 1
    print("attempts left : ", attampts)

    if guess > number:
        print("Value is too high !")

    elif guess < number:
        print("value is too low !")

    else :
        print("you WON :) !")
        break

    

if attampts == 0:
   print("Game over! the number was: ", number)