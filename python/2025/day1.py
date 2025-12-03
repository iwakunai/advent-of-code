# https://adventofcode.com/2025/day/1
pw1 = 0
pw2 = 0

curr = 50
with open("input1.txt", "r") as file:
    for line in file:
        dir = line[0]
        step = int(line.lstrip(dir))
        if dir == "L":
            step *= -1
            # Edge cases for pw2
            # Remove landing on zeros 
            pw2 -= (curr % 100) == 0
            # Add passing zeros
            pw2 += (curr + step) % 100 == 0
       
        curr += step

        pw2 += abs(curr // 100)

        curr %= 100

        if(curr == 0):
            pw1 += 1

print("Password 1:", pw1)
print("Password 2:", pw2)