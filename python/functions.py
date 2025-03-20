# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

price = 0
discount_percent = 0

def calculate_discount(price,discount_percent):
    price = int(input("Enter the price of the item: "))
    discount_percent = int(input("Enter the discount percentage: "))

    if discount_percent >= 20:
        final_price = int(price * (100 - discount_percent) / 100)
        print(f"The final price after applying the discount is: {final_price}")
    else:
        print(f"No discount was applied. The original price is: {price}")


calculate_discount(price, discount_percent)