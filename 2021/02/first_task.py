horizontal = 0  #Value of horizontal movement
depth = 0  #Value of depth movement
forward = 0  #Increases the horizontal position by X units.
down = 0  #Increases the depth by X units.
up = 0  #Decrease the depth by X units.
clean_list = []  #Empty list at first but later a list with all data values
file = open("data.txt", "r")  #Open file
data = file.readlines()  #Make data variable the lines in the file

#remove \n from data
for num in data:
    clean_list.append(num.strip())


for num in clean_list:
    #split data into two parts with delimiter " "
    num = num.split(" ")
    #if the first part is "forward" then increase the horizontal position by the second part
    if num[0] == "forward":
        forward = int(num[1])
        horizontal += forward
    #if the first part is "down" then increase the depth by the second part
    elif num[0] == "down":
        down = int(num[1])
        depth += down
    #if the first part is "up" then decrease the depth by the second part
    elif num[0] == "up":
        up = int(num[1])
        depth -= up

#result is the sum of the horizontal and depth
result = horizontal * depth
print(result)