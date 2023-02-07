import turtle

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

a, degree = 1, 90
t.speed(10)
t.penup()
t.goto(0,200)
t.pendown()

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
    
turtle.done()