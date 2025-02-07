"""
function main()
    get num_items
    total_price = 0.0

    for i in range(num_items)
        get price
        total_price += price

    if total_price > 100
        discount = total_price * 0.10
        total_price -= discount
        display "Discount applied: 10%"

    display "The total price is: ${total_price:.2f}"
main()
"""

def main():
    num_items = int(input("Enter the number of items: "))
    total_price = 0.0

    for i in range(num_items):
        price = float(input(f"Enter the price of item {i + 1}: "))
        total_price += price

    if total_price > 100:
        discount = total_price * 0.10
        total_price -= discount
        print(f"Discount applied: 10%")

    print(f"The total price is: ${total_price:.2f}")
main()