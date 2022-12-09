"day3"
file = open("data.txt", "r")
bags = file.read().splitlines()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upperalphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
totalprio = 0
characterread = False

for bag in bags:
    characterread = False
    items = len(bag)
    pocket1 = bag[:items//2]
    pocket2 = bag[items//2:]
    for character in pocket1:
        if character in pocket2 and characterread is False:
            if character.islower():
                prio = alphabet.index(character)
                prio += 1
                totalprio += prio
                characterread = True
            else:
                prio = upperalphabet.index(character)
                prio += 27
                totalprio += prio
                characterread = True


print(totalprio)
