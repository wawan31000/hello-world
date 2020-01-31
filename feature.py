import math as m
import datetime as dt
import string

print("hello")
# this is  a comment
unit_price = 3
print(unit_price)
unit_price = 'toto'
print(unit_price)
quantity = 1000000
unit_price = 26.99

extended_price = quantity * unit_price
print(extended_price)

if extended_price >= 300:
    extended_price = extended_price * 0.9
elif extended_price >= 200 and extended_price < 300:
    extended_price = extended_price * 0.95
else:
    extended_price = extended_price * 0.98
print(f"{extended_price:,.2f}")

today = dt.date.today()
time = dt.datetime.now()
print(today)

name = 'erwan'

if time.hour > 0 and time.hour < 12:
    phrase = "good morning "
elif time.hour >= 12 and time.hour < 18:
    phrase = "good afternoon "
else:
    phrase = "good evening"

print(phrase+name+"! How are you today?")

students = ["mark", "amber"]
students.insert(1,'toto')
print (students)
