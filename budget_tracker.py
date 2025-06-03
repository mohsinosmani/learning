# budget tracker

def budget_analyzer(income, expense_category):
    total_spend = sum(value for category, value in expense_category)
    remaining_balance = income - total_spend
    return total_spend, remaining_balance

income = int(input("Enter your monthly income: \n"))

expense_category = []
print("Enter expense category, and Type 'done' to finish \n")

while True:
    category = input('Enter expense category: \n')
    if category.lower() == 'done':
        break
    try:
        expense_amount = float(input(f"Enter Value for '{category}': "))
        expense_category.append((category, expense_amount))
    except ValueError:
        print("Please enter a valid number for value.")

print('your monthly income is $', income)
total_spend, remaining_balance = budget_analyzer(income, expense_category)
print('your total spending is: $', total_spend)
print('your remaining balance is: $', remaining_balance)

for category, value in expense_category:
    percent = (value / income) * 100
    warning = " <-- Warning: Over 50% of income!" if percent > 50 else ""
    print(f"- {category}: (${value}) ({percent:.1f}%) {warning}")