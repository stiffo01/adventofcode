file = open("data.txt", "r")
data = file.readlines()
clean_list = []

for num in data:
    clean_list.append(num.strip())

for num in range(0, len(clean_list)):
    clean_list[num] = int(clean_list[num])

last_num = clean_list[0]
incr = 0
for num in clean_list:
    print("Reading", num)
    if num > last_num:
        incr += 1
        print("increase nr", incr)
        last_num = num
    last_num = num
