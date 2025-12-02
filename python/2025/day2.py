invalidA = 0
invalidB = 0

with open ("input2.txt", "r") as file:
    arr = file.readline().split(",")
    for idRange in arr:
        split = idRange.split("-")
        startId = int(split[0])
        endId = int(split[1])

        for id in range(startId, endId + 1):
            idStr = str(id)
            idLen = len(idStr)
            
            for i in range(idLen // 2, 0, -1):
                repeats = idStr.count(idStr[0 : i])
                if repeats == -(-idLen // (i)):
                    invalidA += id if repeats == 2 else 0
                    invalidB += id
                    break

print("Part A:", invalidA)
print("Part B:", invalidB)