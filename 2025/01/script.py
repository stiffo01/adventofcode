def move(inst, rot, tot):
    if inst == 'R':
       print("R")
       print("Before:", tot)
       print("rot:", rot)
       tot = (rot + tot) % 100
       print("After:", tot)
       print("---")
    elif inst == 'L':
        print("L")
        print("Before:", tot)
        tot = (rot - tot) % 100
        print("After:", tot)
        print("---")

    return(tot)
tot=50
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        inst = line[0]
        rot = int(line[1:])
        tot = move(inst, tot, rot)
        print("Total so far:", tot)