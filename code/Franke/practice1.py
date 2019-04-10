##practice 0
def multiply(a,*args):
    return a*sum(args)

#print(multiply(8,2,2,0))

##practice 1 odd or even numbers
def is_even(w):
    return w % 2 == 0


#print(is_even(6))

##practice 2 Positive vs negative numbers
def opposite(q,o):
    return (q > 0 and o < 0) or (q > 0 and o < 0)


#print(opposite(3,2))

##practice 3
# Write a function that returns True if a number within 10 of 100.

def near_100(r):
    return 90 < int(r) < 110

print(near_100(105))

##practice 4
# Write a function that returns the maximum of 3 parameters

def maximum_of_three(a, b, c):
    return max(a,b,c)

#print(maximum_of_three(2,9,4))


##practice 5
# Print out the powers of 2 from 2^0 to 2^20
def powers_of_2():
        for i in range(0,21):
            a = 2*i
            print(a)


print(powers_of_2())