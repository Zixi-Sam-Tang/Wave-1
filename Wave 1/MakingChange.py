import math
cents = int(input())
toonie = math.floor(cents/200)
cents -= toonie * 200
loonie = math.floor(cents/100)
cents -= loonie * 100
quarter = math.floor(cents/25)
cents -= quarter * 25
dime = math.floor(cents/10)
cents -= dime * 10
nickel = math.floor(cents/5)
cents -= nickel * 5
penny = cents
print("toonies:", toonie, "loonies:", loonie, "quarters:", quarter, "dimes:", dime, "nickels:", nickel, "pennies:", cents)