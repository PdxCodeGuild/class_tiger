
jackalopes = [0, 0,]

def age(jackalopes):
    for i in range(len(jackalopes)):
        jackalopes[i] += 1
    return jackalopes

def reproduce(jackalopes):
    for i in range(0, len(jackalopes), 2):
        if  4 <= jackalopes[i] <= 8 and 4 <= jackalopes[i+1] <=8 :
            jackalopes.append(0)
            jackalopes.append(0)
    return jackalopes

def die(jackalopes):
    while True:
        if jackalopes[0] > 10:
            jackalopes.pop(0)
        else:
            break
    return jackalopes

counter = 0
while len(jackalopes) < 1000:
    jackalopes = age(jackalopes)
    jackalopes = die(jackalopes)
    jackalopes = reproduce(jackalopes)
    counter += 1

print(jackalopes)
print(counter)
