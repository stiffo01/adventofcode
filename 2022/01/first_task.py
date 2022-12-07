"the first task"


def calculate_calories():
    elveid = 0
    totcalperelve = 0
    file = open("data.txt", "r", encoding='utf-8')
    elveinventory = file.readlines()
    for calorie in elveinventory:
        if calorie == "\n":
            print("elve", elveid, "totalcal", totcalperelve)
            elveid += 1
            totcalperelve = 0
        else:
            totcalperelve = totcalperelve + int(calorie)


if __name__ == '__main__':
    calculate_calories()
