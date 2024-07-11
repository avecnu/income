
products = ['Bubblegum', 'Toffee', 'Ice cream', 'Milk chocolate', 'Doughnut', 'Pancake']
prices = [2, 0.2, 5, 4, 2.5, 3.2]
earnings = [202, 118, 2250, 1680, 1075, 80]

def income(products, earnings):
    earned = zip(products, earnings)
    temp = 'Earned amount:\n'
    total = 0
    for item, earning in earned:
        total += earning
        temp += f'{item}: ${earning}\n'
    income = f"{temp}\nIncome: ${total}"
    print(income)
    expenses = net_income()
    net = f'Net income: ${total - expenses}'
    print(net)

def net_income():
    print('Staff expenses:')
    staff = int(input())
    print('Other expenses:')
    other = int(input())
    return staff + other

income(products, earnings)