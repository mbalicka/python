def read(fileName):
    try:
        test = open(fileName, "r")
    except FileNotFoundError:
        print("File not found")
        return
    else:
        print(test.read())
        test.close()

def write(text, fileName):
    test = open(fileName, "w")
    test.write(text)
    test.close()

def main():
    fileName = "test2"
    read(fileName)
    write("Ala ma kota.", fileName)
    read(fileName)

if __name__ == "__main__":
    main()