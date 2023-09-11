overs = input("HI there and welcome to this cricket game: Please click enter once you're ready! : ")
OverOne = []
OverTwo = []
OverThree = []
OverFour = []
OverFive = []

while overs != "done":
    over = 0
    i = 0
    if over == 0:
        while i <= 5:
            print("This is over One")
            score = int(input("Score for Over ONE : "))
            OverOne.append(score)
            i += 1
        print("Over One: " + str(OverOne))
        i = 0
        over += 1
    if over == 1:
        while i <= 5:
            print("This is over Two")
            score = int(input("Score for Over Two : "))
            OverTwo.append(score)
            i += 1
        over += 1
        i = 0
        print("Over Two: " + str(OverTwo))   
    if over == 2:
        while i <= 5:
            print("This is over Three")
            score = int(input("Score for Over Three : "))
            OverThree.append(score)
            i += 1
        over += 1
        i = 0
        print("Over Three: " + str(OverThree))  
    if over == 3:
        while i <= 5:
            print("This is over Four")
            score = int(input("Score for Over Four : "))
            OverFour.append(score)
            i += 1
        over += 1
        i = 0
        print("Over Four: " + str(OverFour))  
    if over == 4:
        while i <= 5:
            print("This is over Two")
            score = int(input("Score for Over Five : "))
            OverFive.append(score)
            i += 1
        over += 1
        i = 0
        print("Over Five: " + str(OverFive)) 
        break

print("Over One: " + str(OverOne))
print("Over Two: " + str(OverTwo))   
print("Over Three: " + str(OverThree))  
print("Over Four: " + str(OverFour))
print("Over Five: " + str(OverFive)) 
print("Thanks for playing!!!")
