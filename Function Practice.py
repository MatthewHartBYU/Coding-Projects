def myFunction():
    print("Hello Matthew, how are you today?")
    
def printEach(fruits):
    isFound = False
    for x in fruits:
        if x == "Apple":
            isFound = True  
        print(x)
    if isFound:
        print("Found!")
    else:
        print("Not found!")
    print()
        
def writeToFile():
    word = "Hello"
    filePath = "/Projects/Test.txt"
    #write to the file
    with open(filePath, "w") as curFile:
      curFile.write("Hello world\n")
      curFile.write("This is for testing purposes!")
      #read from the file
    with open(filePath) as curFile:
      for line in curFile:
          print(line,)
          if word in line:
              print(word + " is found!")
def main():
    fruits = ["Apple", "Pear", "Banana"]
    myFunction()
    printEach(fruits)
    writeToFile()
main()
