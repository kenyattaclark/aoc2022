f = open('day1.txt', 'r')
content = f.read()
l = content.split('\n')

currentCalories = 0
mostCalories = 0
currentElf = 0
elfWithMostCalories = 0
calorieArray = []

for s in l:
    if s != '':
        # print(f'Working on elf number: {currentElf + 1} -> {currentCalories} + {s}')
        currentCalories = currentCalories + int(s)
    else:
        currentElf = currentElf + 1
        # print(f'Elf number {currentElf} is carrying {currentCalories} calories')
        calorieArray.append(currentCalories)
        if currentCalories > mostCalories:
            mostCalories = currentCalories
            elfWithMostCalories = currentElf
        currentCalories = 0

print(f'Part 1: The elf carrying the most calories is number {elfWithMostCalories} and they are carrying {mostCalories}.')
calorieArray.sort(reverse=True)
print(f'Part 2: Top 3 Total: {calorieArray[0] + calorieArray[1] + calorieArray[2]}')