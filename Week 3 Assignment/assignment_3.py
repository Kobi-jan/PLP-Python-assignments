def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent/100)
        return final_price
    else:
        return price
    

# User inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

# Print result
print(f"The final price after the discount of {discount_percent}% is {final_price:.2f}")

