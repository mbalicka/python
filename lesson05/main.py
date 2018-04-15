def main():
    tmpString = "new"
    age = 27
    print("something %s" % tmpString)
    print(tmpString * 10)
    print("I am %d years old" % age)

    # part 2
    pi = 3.1415
    print("Pi is equal %f" % pi)
    print("Pi with two decimal points is equal %.2f" % pi)
    print("Pi as integer is equal %d" % pi)
    print("Pi as integer is equal %.0f" % pi)

    # part 3
    myData = ("Maria", 27, 1.7)
    print("My name is %s, I'm %d years old and I am %.1fm high" % myData)

if __name__ =="__main__":
    main()