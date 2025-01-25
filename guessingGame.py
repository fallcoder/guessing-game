import random

randnum = random.randint(1, 101)

def computerGuess(lowval, highval, randnum, count=0, guesses=[]):
    if highval >= lowval:
        #calculate the computer's guess
        guess = lowval + (highval - lowval) // 2
        guesses.append(guess)
        if guess == randnum:
            print(f"computer's guesses : {guesses}")
            return count
        elif guess > randnum:
            count += 1
            return computerGuess(lowval, guess-1, randnum, count, guesses)
        else:
            count += 1
            return computerGuess(guess + 1, highval, randnum, count, guesses)
    else:
        return -1

count = 0
guess = None

while guess != randnum:
    try:
        #get the user's guess
        guess = int(input("enter your guess btw 1 and 100 : "))
        if guess < 1 or guess > 100:
            print("your guess is out of range! please enter a number btw 1 and 100 ")
            continue
        if guess < randnum:
            print("higher")
        elif guess > randnum:
            print("lower")
        else:
            print("you guessed it")
            break
        count += 1
    except ValueError:
        print("invalid input! please enter a valid number ")
    
print("you took " + str(count) + " steps to guess the number  ")  
print("computer took " + str(computerGuess(0,100, randnum)) + " steps")