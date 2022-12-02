f = open('day1.txt', 'r')
content = f.read()
l = content.split('\n')

currentCalories = 0
calorieArray = []

for s in l:
    if s != '':
        currentCalories = currentCalories + int(s)
    else:
        calorieArray.append(currentCalories)
        currentCalories = 0

calorieArray.sort(reverse=True)
print(f'Part 1: The most calories carried by an elf is {calorieArray[0]}')
print(f'Part 2: Top 3 Total: {calorieArray[0] + calorieArray[1] + calorieArray[2]}')