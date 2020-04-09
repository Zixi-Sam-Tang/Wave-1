money = int(input())
for i in range(1, 4):
    money *= 1.04
    print("year " + str(i) + ": $" + "{:.2f}".format(money))