import numpy


def f1(x):
    return x**3 - 3


def df1(x):
    return 3*x**2


def f2(x):
    return 5*x + numpy.log(x) - 10000


def df2(x):
    return (1/x) + 5


def f4(x):
    return 10


def df4(x):
    return 0


def newtonraphson(f, df, x0, iterations=10, tol=0.005):
    guess = x0
    it = 1

    while it <= iterations:
        old_guess = guess
        guess -= f(guess) / df(guess)
        # print("guess" + str(iter) + ": " + str(guess))

        if abs(guess - old_guess) <= tol:
            print("Under tol(" + str(tol) + ") in " + str(it) + " iterations")
            return guess

        it += 1
    print("Hit max interations: " + str(iterations))
    return guess


def oppgave1():
    print("Oppgave 1")
    x3 = newtonraphson(f1, df1, x0=2.5, iterations=3)
    print(x3)
    print()


def oppgave2():
    print("Oppgave 2")
    print(newtonraphson(f2, df2, x0=1000, tol=1*10**-6))
    print()


def oppgave4():
    print("Oppgave 4")
    print(3.16227766)
    print()

oppgave1()
oppgave2()
oppgave4()
