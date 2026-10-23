def readnwriteFile(inputFileName, outputFileName):
    listInput = []
    listOutput = []
    i = 0
    with open(inputFileName, 'r') as file:
        listLines = file.readlines()
        for line in listLines:
            listInput.append(listLines[i])
            i += 1
        print("Input File Contents:")
        printList(listInput)
        file.close()
    with open(outputFileName, 'w') as file:
        line1 = "This is cool"
        line2 = "This is funny"
        file.write(line1)
        file.write(line2)
        listOutput.append(line1)
        listOutput.append(line2)
        print("Output File Contents:")
        printList(listOutput)
        file.close()
def printList(list):
    i = 0
    while i<len(list):
        print(list[i],end="\n")
        i+=1
def main():
    readnwriteFile("FunnyStuff.txt", "MoreFunnyStuff")
main()