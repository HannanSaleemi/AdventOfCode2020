# Open input and store as arr
inputArr = []
f = open("input.txt")
for line in f:
    inputArr.append(int(line))

inputArr = sorted(inputArr)


# Two Numbers
left = 0
right = len(inputArr)-1

while (left < right):
    currentSum = inputArr[left] + inputArr[right]
    if currentSum == 2020:
        print("Numbers are: {} and {}".format(inputArr[left], inputArr[right]))
        print("Answer: {}".format(inputArr[left] * inputArr[right]))
        break
    elif currentSum > 2020:
        right -= 1
    else:
        left += 1


# Three Numbers
# Static pointer going through all, and then Two Pointers on the rest
for staticPointer in range(0, len(inputArr) - 2):
    tripleSum = 2020 - inputArr[staticPointer]
    if tripleSum > 0:
        left = 0
        right = len(inputArr)-1
        while (left < right):
            if (left == staticPointer):
                left += 1 
                continue
            tempSum = inputArr[left] + inputArr[right] + inputArr[staticPointer]
            if (tempSum == 2020):
                print("Three Numbers Are: {}, {}, {}".format(inputArr[left], inputArr[right], inputArr[staticPointer]))
                print(inputArr[left] * inputArr[right] * inputArr[staticPointer])
                break
            elif (tempSum > 2020):
                right -= 1
            else:
                left += 1
    else:
        continue
            