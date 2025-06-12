print("Take a guess")
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit :
    guess_count += 1
    guess = int(input("Guess: "))
    
if guess == secret_number:
    print("You won!")

else:
    print("Oops you lost")
