with open ("input.txt", "r") as file:
    data = file.read()
    print(data)

#search for the biggest number in each line of data
lines = data.splitlines()
biggest_numbers = []
for line in lines:
    numbers = line.split()
    print(numbers)
    for number in numbers:
        nextnumber = int(number) + 1
        if number > nextnumber:
            highnum1 = number
        