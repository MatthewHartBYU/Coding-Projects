def isQualified(listName,listG,listS, listScores):
    #a student is qualified if there GPA is greater than or equal 3.8
    i = 0
    for GPA in listG:
        if float(GPA) >= 3.8:
            print(f"Student {listName[i]} has an average score of {listScores[i]} is qualified with a GPA of {GPA} and is admitted to {listS[i]}")
        else:
            print(f"Student {listName[i]} has an average score of {listScores[i]} and is not qualified with a GPA of {GPA} and is not admitted to {listS[i]}")
        i+=1
def calcAverageScore(listGrades):
    sumGrades = 0
    for grade in listGrades:
        sumGrades += int(grade)
    return round((sumGrades/len(listGrades)),2)
def retrieveData():
    file = open("Names.txt","r")
    data = file.readlines()
    listNames = []
    listGPAs =  []
    listSchools = []
    listGrades = []
    for line in data:
        line = line.replace("\n","")
        curData = line.split(",")
        listNames.append(curData[0])
        listGPAs.append(curData[1])
        listSchools.append(curData[2])
        curGradeSet= [curData[i] for i in range (3,len(data)+1)]
        listGrades.append(curGradeSet)
    listAverageScores = []
    for gradeSet in listGrades:
        score = calcAverageScore(gradeSet)
        listAverageScores.append(score)
    isQualified(listNames,listGPAs,listSchools, listAverageScores)

def main():
    retrieveData()
main()