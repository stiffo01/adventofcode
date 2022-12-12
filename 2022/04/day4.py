"Day 4"
file = open("data.txt", "r")
segments = file.read().splitlines()
contain = 0


def is_individual1_in_individual_b(contain, individual1, individual2):

    check = any(item in individual1 for item in individual2)
    if check is True:
        print("some is same")
        if individual1[0] == individual1[1]:
            if individual1[0] > individual2[0] and individual1[0] <= individual2[1]:
                print("its inside")
                contain += 1
            else:
                print("inte i")
        return print("The list {} contains some elements of the list {}".format(individual1, individual2))


def beforeorafter(contain, individual1, individual2):
    if individual1[0] < individual2[0] and individual1[1] < individual2[0]:
        print(individual1, "is before other list", individual2)
    elif individual1[0] > individual2[0] and individual1[0] > individual2[1]:
        print(individual1, "after other list", individual2)

    elif individual1[0] > individual2[0] and individual1[0] < individual2[1]:
        print(individual1, "is inside", individual2)
        contain += 1


for elvepair in segments:
    elvepair = elvepair.split(",")

    individual1 = elvepair[0].split("-")

    individual2 = elvepair[1].split("-")

    is_individual1_in_individual_b(contain, individual1, individual2)

print(contain)
