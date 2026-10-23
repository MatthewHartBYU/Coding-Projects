def oddValues(nums):
    #return all the numbers at the odd indexes of a file
    oddNums = []
    i = 0
    while i< len(nums):
        if i % 2 != 0:
            oddNums.append(nums[i] * i)
        i+=1
    return oddNums
def replaceNums(nums):
    #replace all the even values with 0 in the array and the odd values with 1
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            nums[i] = 0
        else:
            nums[i] = 1
        i+=1
    return nums
#return the largest value in a list
def findLargest(nums):
    i = 0
    while i<len(nums):
        largestNum = nums[i]
        if nums[i] > largestNum:
            largestNum = nums[i]
        i+=1
    print(largestNum)
#return the smallest value in a list
def findSmallest(nums):
    smallestNum = nums[0]
    for num in nums[1:]:
        if num < smallestNum:
            smallestNum = num
    print(smallestNum)
#Reverse a list of numbers
def reverseList(nums):
    reversedList = []
    i = len(nums)
    for j in range(0,len(nums)):
        reversedList.append(nums[i-1])
        i-=1
    print(reversedList)
def reverseNum(n):
    numString = ""
    while n != 0:
        digit = n % 10
        numString += str(digit)
        n //= 10
    return int(numString)
#sum a list recursively
def sumList(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sumList(nums[1:])
#reverse a string recursively
def reverseString(word):
    if len(word) == 0:
        return ""
    else:
        return word[-1] + reverseString(word[:-1])
#sum a number recursively
def sumNumber(num):
    if num == 0:
        return 0
    else:
        return (num%10) + sumNumber(num//10)
def main():
    nums = [2,5,1,8,9,13,21,123,1567]
    nums2 = [2,3,4,5,2,3,6]
    findSmallest(nums)
    findLargest(nums)
    reverseList(nums2)
    print(reverseNum(567))
    print(sumList(nums))
    print(reverseString("Hello Brother"))
    print(sumNumber(1245))
main()