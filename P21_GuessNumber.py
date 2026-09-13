num = 40  

for i in range(10):   
    guess = int(input("Enter your guess: "))

    if guess == num:
        print("Correct number:", num)
        break
    elif guess > num:
        print("Too high! Try again")
    else:
        print("Too low! Try again")
else:
    print("Sorry, you used all attempts and The number was", num)
