def isAscending(listNums):
    listSortedNums = sorted(listNums)
    return listNums == listSortedNums

def main():
    listNums = [1,2,1,3,4]
    print(isAscending(listNums))


main() 
