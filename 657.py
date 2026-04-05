
def judgeCircle(moves) -> bool:
    X = 0
    Y = 0
    for k in moves:
        if (k == "U"):
            X +=1
        if (k == "D"):
            X -= 1
        if (k == "R"):
            Y +=1
        if (k == "L"):
            Y -= 1
    value = X - Y
    print (value)
    if (X ==0 and Y == 0):
            return True 
    else: 
            return False 

thing = judgeCircle(["D","U","L","R"])
thing2 = judgeCircle(["D","U","L","R","R"])
print(thing2)