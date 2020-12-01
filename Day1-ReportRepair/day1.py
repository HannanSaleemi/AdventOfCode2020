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


