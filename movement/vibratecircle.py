import turtle
import time

def isPrime(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True




t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")

size = 100000
degree = 90
lastCorner, apoio, countNrCornersPerSize = 1, 1, 0
t.speed("fastest")
t.penup()
t.goto(0,0)
t.pendown()

#disable animation
s.tracer(0, 0)

for i in range(1,size):
    print(i)
    if isPrime(i):
        t.dot(5, "blue")
        
    lastCorner -= 1
    t.forward(10)
    
    if lastCorner == 0:
        countNrCornersPerSize += 1
        if countNrCornersPerSize == 2: 
            apoio += 1
            countNrCornersPerSize = 0
        lastCorner = apoio
        t.left(degree)

#update cause the animation is disabled
turtle.update()
"""
while True:
    print(a/10)
    print(isPrime(a/10))
    print("---------------------")
    t.forward(a)
    t.right(degree)
    if isPrime(a/10) :
        t.dot(20, "blue")
    t.forward(a)
    t.right(degree)
    if isPrime(a/10) :
        t.dot(20, "blue")
    a+=10
    t.hideturtle()
"""
turtle.done()