file = open("data.txt", "r")  # Open the data file and read it
data = file.readlines()  # Get all numbers in file on one line
clean_list = []  # List with all data
increment = 0  # Variable counting how many times the reading has incremented
three = 0
last_three = 0
# Get rid of \n after every number
for num in data:
    clean_list.append(num.strip())

# Make the numbers str>int
for num in range(0, len(clean_list)):
    clean_list[num] = int(clean_list[num])


def incrementfunction():
    global increment
    increment += 1
    print("incremented with 1 now increment number is:", increment)


def three_avg_start_value():
    global three
    three = clean_list[0] + clean_list[1] + clean_list[2] // 3
    print("Divided by 3", three)


def three_avg(i):
    global three
    i += 2
    a = i
    print("a is ", a)
    i += 1
    b = i
    print("b is ", b)
    i += 1
    c = i
    print("c is ", c)
    three = int(clean_list[a]) + int(clean_list[b]) + int(clean_list[c]) // 3
    print("Divided by 3", three)


for num in range(0, len(clean_list)):
    print("The reading is:", clean_list[num])
    print("List number:", num)
    if num == 0:
        three_avg_start_value()
    else:
        three_avg(num)
        if three > last_three:
            incrementfunction()
        else:
            print("No increment")
