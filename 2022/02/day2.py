"day 2"
SCORE = 0 


def play():
    global SCORE
    with open("data.txt") as file: # Use file to refer to the file object
        game = file.read().splitlines()
        print(game)
        for hands in game:
            elvehand = hands[0]
            myhand = hands[2]
            if myhand == "X":
                myhand = "A"
            elif myhand == "Y":
                myhand = "B"
            else:
                myhand = "C"
            handshape(myhand)
            
            if elvehand == myhand:
                draw()
            elif myhand == "A":
                if elvehand == "C":
                    win()
            elif myhand == "B":
                if elvehand == "A":
                    win()
            elif myhand == "C":
                if elvehand == "B":
                    win()
    print(SCORE)


def win():
    global SCORE
    SCORE += 6
    print(SCORE)
    return SCORE
 

def draw():
    global SCORE
    SCORE += 3
    return SCORE
 

def handshape(shape):
    global SCORE
    if shape == "A":
        SCORE += 1
    elif shape == "B":
        SCORE += 2
    else:
        SCORE += 3
    return SCORE
 

if __name__ == '__main__':
    play()
