import pandas as pd
import openpyxl
import re
from recommendedprices import recommended_prices

def calculate_profit(product_key, product_volume, sell_price):
    # Find the product in the data
    product = df[df['Material Name'].apply(lambda x: product_key in x and re.search(rf"{product_volume}\D*", x) is not None)]
    if len(product) == 0:
        return "Product not found."

    # Calculate profit
    buy_price = product['new price'].values[0]
    profit = sell_price - buy_price
    return profit

# Load the data
df = pd.read_excel('Book1.xlsx', engine='openpyxl')

def find_product(df, key, volume, sell_price):
    # Convert volume to int
    volume = int(volume) if volume else None

    subset = df[df['Material Name'].apply(lambda x: key in x and re.search(rf"{volume}\D*", x) is not None)]

    # Check if product exists
    if subset.empty:
        print('Product not found.')
        return None

    # Extract 4-digit code from product name
    code = re.search(r'\d{4}', subset['Material Name'].iloc[0]).group(0)

    for index, row in subset.iterrows():
        print("Product Code:", row["Material Code"])
        print("Product Name:", row["Material Name"])
        print("Cost Price:", row["new price"])
        profit = sell_price - row["new price"]
        profit_percentage = (profit / row["new price"]) * 100
        print("Profit:", profit)
        print("Profit Percentage:", profit_percentage)
        print("------")

    # If the product code and volume are in the recommended_prices dictionary
    if code in recommended_prices and volume in recommended_prices[code]:
        rec_price_küçük = recommended_prices[code][volume]["KÜÇÜK"]
        rec_price_büyük = recommended_prices[code][volume]["BÜYÜK"]
        profit_küçük = sell_price - rec_price_küçük
        profit_büyük = sell_price - rec_price_büyük
        profit_percentage_küçük = (profit_küçük / rec_price_küçük) * 100
        profit_percentage_büyük = (profit_büyük / rec_price_büyük) * 100
        print(f"Recommended price (KÜÇÜK): {rec_price_küçük:.2f}")
        print(f"Profit (KÜÇÜK): {profit_küçük:.2f}")
        print(f"Profit percentage (KÜÇÜK): {profit_percentage_küçük:.2f}%")
        print(f"Recommended price (BÜYÜK): {rec_price_büyük:.2f}")
        print(f"Profit (BÜYÜK): {profit_büyük:.2f}")
        print(f"Profit percentage (BÜYÜK): {profit_percentage_büyük:.2f}%")

    return subset


while True:
    user_input = input("Enter the product key and volume (or 'quit' to stop): ")
    if user_input.lower() == 'quit':
        break
    else:
        user_input_split = user_input.split()
        if len(user_input_split) == 1:
            key = user_input_split[0]
            volume = None  # Volume is not provided
        elif len(user_input_split) == 2:
            key, volume = user_input_split
        else:
            print("Invalid input. Please provide a product key and optionally a volume.")
            continue

        sell_price = float(input("Enter the sell price: "))
        occurrences = find_product(df, key, volume, sell_price)

