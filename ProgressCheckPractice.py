#in this first part of the exercise, sum the numbers in the file and return the average
def sumAverage(filename):
    file = open(filename, "r")
    data = file.readlines()
    sumNums = 0
    for line in data:
        sumNums += int(line)
    print(f"Average of numbers in file: {sumNums/len(data):.2f}")
def computeStudentData(filename):
    file = open(filename,"r")
    data = file.readlines()
    scoreMelbourne = 0
    scoreAustin = 0
    outputFile = open("Scores.txt","w")
    studentInfo = {"Melbourne":0, "Austin":0, "LongestName":0, "ShortestName":0,"AverageNameLength":0,"RNames":0, "EvenLengthNames":0, "OddLengthNames":0}
    studentNames = []
    lengthNames = 0
    for line in data:
        line = line.strip().split(",")
        if "Melbourne" in line:
            scoreMelbourne += int(line[2])
            studentInfo["Melbourne"] += 1
        if "Austin" in line:
            scoreAustin += int(line[2])
            studentInfo["Austin"] += 1
        studentNames.append(line[0])
        lengthNames += len(line[0])
    outputFile.write(str(scoreAustin))
    outputFile.write("\n")
    outputFile.write(str(scoreMelbourne))
    studentInfo["LongestName"] = max(studentNames, key=len)
    studentInfo["ShortestName"] = min(studentNames, key=len)
    studentInfo["AverageNameLength"] = int(lengthNames/len(studentNames))
    outputFile.write("\n")
    for curName in studentNames:
        if "R" in curName:
            studentInfo["RNames"] += 1
        if len(curName) % 2 == 0:
            studentInfo["EvenLengthNames"] += 1
        if len(curName) & 2 == 0:
            studentInfo["OddLengthNames"] += 1
    for key,value in studentInfo.items():
        userString = key + ": " + str(value)
        outputFile.write(userString)
        outputFile.write("\n")

def main():
    sumAverage("nums.txt")
    computeStudentData("students.text")
main()