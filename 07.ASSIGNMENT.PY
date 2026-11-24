#Calculate Daily Calorie Intake

def calculate_calories(carbs,fats,proteins):
    total = (carbs * 4) + (fats * 9) + (proteins * 4)
    return total

carbs = float(input("Enter the amount of carbohydrates (in grams): "))
fats = float(input("Enter the amount of fats (in grams): "))
proteins = float(input("Enter the amount of proteins (in grams): "))    

total = calculate_calories(carbs,fats,proteins)

print("Total daily calorie intake is:", total)