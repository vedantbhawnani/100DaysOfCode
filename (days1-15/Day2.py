print("Welcome to the Tip Calculator.")
total = float(input('What was the total bill amount?'))
people = int(input('How many people to split the bill between?'))
tip = int(input('What percentage of tip you would like to give? 10, 12, or 15?'))

print('Each person should pay: {:.1f}'.hformat((total + total*(tip/100))/5))
