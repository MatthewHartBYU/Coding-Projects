def numOccurences(nums, targetNum):
    numOcc = 0
    for num in nums:
        if num == targetNum:
            numOcc += 1
    print(numOcc)
def main():
     nums = [3,5,2,1,6,3,3,4,5]
     numOccurences(nums,3)
main()