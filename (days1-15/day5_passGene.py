import random
import string

length = int(input("How many letters? "))
symbols = input("How many symbols? ")
numb = input("how many numbers wouuld you like? ")

symbols = ['!', '@', '#', '$', '%', '^', '&',
           '*', '(', ')', '?', '\\', '|', '', '+', '-', ]

passw = ''.join([random.choice(string.ascii_letters +
                string.digits+random.choice(symbols)) for i in range(length)])

print(passw)
