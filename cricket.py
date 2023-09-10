overs = input("HI there which over is it? please type an integer and once done please type: done").lower()
OverOne = []
OverTwo = []
OverThree = []
OverFour = []
OverFive = []

while overs != "done":
    over = 0
    if over == 0:
        for i in range(5):
            print("This is over One")
            score = int(input("Score for Over ONE : "))
            OverOne.append(score)
        over += 1
        print("Over One: " + str(OverOne))
    elif over == 1:
        for i in range(5):
            print("This is over Two")
            score = int(input("Score for Over Two : "))
            OverTwo.append(score)
        over += 1
        print("Over Two: " + OverTwo)   
    elif over == 2:
        for i in range(5):
            print("This is over Three")
            score = int(input("Score for Over Three : "))
            OverThree.append(score)
        over += 1
        print("Over Three: " + OverThree)  
    elif over == 3:
        for i in range(5):
            print("This is over Four")
            score = int(input("Score for Over Four : "))
            OverFour.append(score)
        over += 1
        print("Over Four: " + OverFour)  
    elif over == 4:
        for i in range(5):
            print("This is over Two")
            score = int(input("Score for Over Five : "))
            OverFive.append(score)
        over += 1
        print("Over Five: " + OverFive) 
    else:
        print("The final score was : " + str(OverOne + OverTwo + OverThree + OverFive + OverFour) + " runs.") 