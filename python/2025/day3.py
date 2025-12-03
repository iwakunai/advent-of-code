output1 = 0
output2 = 0
with open ("input3.txt" , "r") as file:
    for line in file:
        data = line.strip()
        d1 = line[0]
        d2 = line[1]
        for i in range(1, len(data)):
            if data[i] > d1 and i < len(data) - 1:
                d1 = data[i]
                d2 = data[i+1]
            elif data[i] > d2:
                d2 = data[i]

        output1 += int(d1) * 10 + int(d2)
        print(int(d1) * 10 + int(d2), output1)


print("Output Joltage 1:", output1)
print("Output Joltage 2:", output2)