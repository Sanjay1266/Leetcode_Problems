
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
    return(value)

thing = judgeCircle(["D","U","L","R"])