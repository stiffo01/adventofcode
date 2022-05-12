gamma_rate = 0
epsilon_rate = 0
clean_list = []  #Empty list at first but later a list with all data values
file = open("data.txt", "r")  #Open file
data = file.readlines()  #Make data variable the lines in the file
one = 0
zero = 0
a = 0
#remove \n from data
for num in data:
    clean_list.append(num.strip())

#function for calculating clean_list first number divided by total list length
def gamma_calculator(clean_list):
    global zero, one
    global a
    #check first number in list
    for num in clean_list:
        #count if 1 or 0
        if num[a] == "1":
            one += 1
        else:
            zero += 1
            
    # calculate wich variable is bigger
    if one > zero:
        gamma_rate = 1
    elif one < zero:
        gamma_rate = 0
    
    print("one is", one ,"and zero is", zero, "and gamma rate is: ",gamma_rate)
    
        
def epsilon_calculator(clean_list):
    global zero, one
    global a
    #check first number in list
    for num in clean_list:
        #count if 1 or 0
        if num[a] == "1":
            one += 1
        else:
            zero += 1
            
    # calculate wich variable is bigger
    if one < zero:
        epsilon_rate = 1
    elif one > zero:
        epsilon_rate = 0
    
    print("one is", one ,"and zero is", zero, "and epsilon rate is: ",epsilon_rate)

        
#run gamma_calculator function 5 times
for i in range(12):
    gamma_calculator(clean_list)
    a += 1
    zero = 0
    one = 0
a = 0
for i in range(12):
    epsilon_calculator(clean_list)
    a += 1
    zero = 0
    one = 0