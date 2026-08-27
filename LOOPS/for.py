
#It will print numbers from 0 to 4 (starting idx from 0 to range)
#It will not print the last element
for i in range(5):
    print(i)

#you can define starting and ending of range
#It will start from 3 to 7
for i in range(3,8):
    print(i)

#we can define the interval to skip while printing the i
#suppose I want to skip every number after the interval of 2
#but here it also assume the starting number as 1 skip
for i in range(3,12,2):
    print(i)


#In PYTHON we can also print in reverse manner or from backwards like
#using -ve indexing: (start, end, iterval(if any))
# Counting backwards from 10 down to 1
for i in range(10, 0, -1):
    print(i)
