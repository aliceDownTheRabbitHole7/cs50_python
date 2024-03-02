# Initial amount of money due

amount_due = 50

# Request money until the due is fulfilled

while amount_due > 0:
    print(f'Amount due: {amount_due}')
    piece = int(input('Insert coin: '))
    if piece in [5, 10, 25]:
        amount_due -= piece

# Calculate the change owed back to the user, if any

change = abs(amount_due)

# Print result to console

print(f'Return change: {change} cents')
