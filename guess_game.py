import random
Username=input("what is your name:")
print("Welcome!",Username)
guess_limit = 3
guesses = 0
while guesses < guess_limit:
  Lottery=(random.randint(0, 100))
  guess_number=int(input("guess a number:"))
  guesses +=1
if guess_number==Lottery:
    print("You guess right")
else:
    print("you are wrong")
    print("the number is:",Lottery)
print("Thanks")