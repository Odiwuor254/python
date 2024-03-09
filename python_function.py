def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# Example values
original_price = 40  # Original price of the item
discount_percentage = 10  # Discount percentage

# Calculating and printing the final price
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after applying the discount:", final_price)
