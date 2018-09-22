#Exercise A
print ("what is your name?")
name = input ("> ")

#Exercise B
print (f"Welcome {name}")

print()
print("Welcome to the dungeon!")
print(f"{name}, do you go through door 1 or door 2?")

door=input("> ")

if door =="1":
    print("There is a nice Vampire asking you if you enjoy life")
    print("What do you do?")
    print("1. smile and nod")
    print("2. Scream and run")

    vampire = input (" >")

    if vampire =="1":
        print (f"Congratulations {name}, you found a new friend!")
    elif vampire =="2":
        print(f"sorry {name}, the vampire is faster. YOu become a dinner!")
    else:
        print("You are not so good with numbers, are you?")

if door =="2":
    print ("there is an old german vampire show master behind door 2 - ¯\_(ツ)_/¯")
    print ("what do you do?")
    print ("1.take the ugly red plush animal and wave to the imaginary audience")
    print (f"2. scream and run - 🧛 will eat you, {name}️")

    vampire =input (" >")

    if vampire =="1":
        print ("congratulations, you got a plush toy!")
    elif vampire =="2":
        print ("how did you end up here? go back and rethink your life!")
    else:
        print ("there are no other options!")

#Excercise D
print ("what is your favorite color?")
color = input("> ")