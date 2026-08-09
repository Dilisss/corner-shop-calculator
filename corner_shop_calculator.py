print('Earned amount:')
print('Bubblegum: $202')
print('Toffee: $118')
print('Ice cream: $2250')
print('Milk chocolate: $1680')
print('Doughnut: $1075')
print('Pancake: $80')

result = 202 + 118 + 2250 + 1680 + 1075 + 80

print()
print('Income: $' + str(result))

print('Staff expenses:')
staff = int(input())

print('Other expenses:')
other_expenses = int(input())

net_income = result - staff - other_expenses

print('Net income: $' + str(net_income))
