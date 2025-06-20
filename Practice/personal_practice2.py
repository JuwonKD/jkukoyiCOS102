car = input("> ")
help_input = input("> ")

if car == "help" :
    print("start - to start the car ")
    print("stop - to stop the car")
    print("quit - to exit")

else:
    print("I don't understand that ...")

if help_input == "start" :
    print("Car started ...Ready to go!")

if help_input == "stop" :
    print("Car stopped")

