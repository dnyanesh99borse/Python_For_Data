#------------FUNCTION-----------------------
#function is a reusable block of code which performs any specific task
#In python we define function using keyword: "def"

def greet():
    print("hello!")

greet()  #print function's output


def add(a,b):
    print(a+b)

print(add(10, 20))

#---------RETURN STATEMENT-------
def add(a, b):
    return a + b

result = add(40, 20)
print(result)

#print() : Displays something on the screen.
# return : Sends a value back from the function.

#------------return multiple values----
def calculate(a, b):
    return a + b, a - b

addition, substraction = calculate(10, 5)

print(addition)
print(substraction)

#---------you can give default parameters values like: -----------------
def greet(name = "Guest"):
    print("Hello", name)

greet()


def student(age=22, name="Dnyanesh"):
    print(name, age)

student()

#------------*args-------------
#sometimes you don't know how many arguments will be passed
def add(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(add(10,20))
print(add(10,20,30))
print(add(10,20,40,50))


#------------**kwargs-------------
# **kwargs allows you to accept multiple keyword arguments.
def student(**details):
    print(details)


student(
    name = ("Dnyanesh"),
    age = 22,
    brach = "Information Technology"
)



