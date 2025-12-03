def largestJoltage(input : str, batteries : int):
    currJoltage = list(input[0:batteries])

    minDigit = min(currJoltage)
    minIndex = currJoltage.index(minDigit)

    lastIndex = len(currJoltage)

    for i in range(batteries, len(input)):
        d = input[i]
        flag = True
        for idx in range(lastIndex - 1):
            if currJoltage[idx] < currJoltage[idx + 1]:
                currJoltage.pop(idx)
                currJoltage.append(d)
                flag = False
                break
        
        if flag and d > minDigit:
            currJoltage.pop(minIndex)
            currJoltage.append(d)

        minDigit = min(currJoltage)
        minIndex = currJoltage.index(minDigit)

    return int("".join(currJoltage))

output1 = 0
output2 = 0
with open ("input3.txt" , "r") as file:
    for line in file:
        data = line.strip()
        ## Old Part A
        # d1 = line[0]
        # d2 = line[1]
        # for i in range(1, len(data)):
        #     if data[i] > d1 and i < len(data) - 1:
        #         d1 = data[i]
        #         d2 = data[i+1]
        #     elif data[i] > d2:
        #         d2 = data[i]
        # output1 += int(d1) * 10 + int(d2)

        output1 += largestJoltage(data, 2)
        output2 += largestJoltage(data, 12)

print("Output Joltage 1:", output1)
print("Output Joltage 2:", output2)