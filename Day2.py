# In this challenge you have to calculate the total rounded cost of a meal after tips and tax are applied

mealCost = float(raw_input())
tipPrecent = int(raw_input())
taxPrecent = int(raw_input())
tip = mealCost * tipPrecent / 100 
tax = mealCost * taxPrecent /100

totalCost = mealCost + tip + tax
roundedCost = round(totalCost)
print "The total meal cost is " + str(int(roundedCost)) + " dollars."