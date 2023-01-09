"day 5"

with open("data.txt") as file:
    stack_strings , instructions = (i.splitlines() for i in file.read().strip("\n").split("\n\n"))

stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ", "")}

indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]

def printstacks():
    "print stacks"
    print("\n", "stacks:", "\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")

def loadstacks():
    """load stacks"""
    for string in stack_strings[:-1]:
        stacknumber = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stacknumber].insert(0, string[index])
            stacknumber += 1


def emptystacks():
    "empty stacks"
    for stacknumber in stacks:
        stacks[stacknumber].clear()

for instruction in instructions:
    instruction = instruction.replace("move", "").replace\
    ("from ", "").replace("to ", "").strip().split(" ")
    print(instruction)


loadstacks()
printstacks()
