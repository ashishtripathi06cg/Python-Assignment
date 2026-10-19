################################## Type Casting =>
#Question 1:-
age = "25"
age = int("25")
print(type(age))

#Question 2:-
marks = "75.5"
marks= float("75.5")
print(marks)
print(type(marks))

#Question 3:-
number = 50
number = float(50)
print(number)
print(type(number))

#Question 4:-
marks =85.9
marks = int(85.9)      ### the decimal part is removed from here ###
print(marks)
print(type(marks))

#Question 5:-
rool_number = 101
rool_number = int(101)
print(rool_number)
print(type(rool_number))

#Question 6:-
num1 = "18"
num1 = int("18")
print(num1)
print(type(num1))


num2 = "92.5"
num2 = float("92.5")
print(num2)
print(type(num2))


num3 = 100
num3 = str(100)
print(num3)
print(type(num3))


num4 = 45.8
num4 = int(45.8)
print(num4)
print(type(num4))

#Question 7:-
a = "20"
b = int(a)

c = 10.8
d = int(c)

e = 25
f = str(e)

print(b)        #20
print(d)        #10
print(f)        #"25"
print(type(b))  # integer
print(type(d))  #int
print(type(f))  #string


#Question 8:-
age = int("19")
new_age = (age + 1)

print("Age:", new_age)