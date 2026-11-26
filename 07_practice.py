#Calorie calculator with percentages
#Take carbs, fats and proteins in grams. Print the total calories and the percentage contributed by each, all to 2 decimals.

def calorie_calculator (carbs,fats,proteins):
    return carbs*4 +fats*8+proteins*4

carbs = float(input("enter intake of carbs:"))
fats = float(input("Enter intake of fats:"))
proteins = float(input("Enter inatke of proteins:"))

total = calorie_calculator(carbs,fats,proteins)
print(f"Total calories = {total:.2f}")

if total>0:
    print(f"Carbs = {carbs*4/total *100:.2f}%")
    print(f"fats = {fats*8/total *100:.2f}%")
    print(f"Proteins = {proteins*4/total *100:.2f}%")