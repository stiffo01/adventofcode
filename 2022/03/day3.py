"day3"
file = open("data.txt","r")
bags = file.read().splitlines()
occurances = []
for bag in bags:
    items = len(bag)
    occurances.append(["pocketstart"])
    pocket1 = bag[:items//2]  
    occurances.append(pocket1)
    occurances.append(["pocketmiddle"])
    pocket2 = bag[items//2:]
    occurances.append(pocket2)
    occurances.append(["pocketend"])
print(occurances)
