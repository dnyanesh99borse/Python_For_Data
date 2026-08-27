# While Loop

i = 0
while i <= 10:
    print(i)
    i = i+1

#output: 0,1,2,3,4,5,6,7,8,9,10

#-----------BREAK STATEMENT------------------
j = 1
while j <= 10:
    if j == 5:
        continue

    print(j)
    j += 1


#-----------CONTINUE----------------------
for j in range(1, 11):
    if j == 5:
        continue
    print(j)


#----------------PASS------------------------
#It's useful when Python requires a statement but you haven't implemented the logic
for i in range(5):
    pass


