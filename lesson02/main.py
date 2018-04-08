def factorialLoop(value):
    fact = 1
    for i in range(1, value + 1):
        fact = fact * i
    return fact

def factorialRec(value):
    if value is 1:
        return 1
    return value * factorialRec(value - 1)

def main():
    fact50 = factorialLoop(50)
    fact120 = factorialLoop(120)
    print(fact50)
    print(fact120)

if __name__ == "__main__":
     main()
