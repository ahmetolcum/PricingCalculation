Product Profit Calculator

This repository contains a Python script that calculates the profit and profit percentage for products based on the provided sell price. It utilizes the pandas library to load and process data from an Excel file.

Features
Product Search: The script allows users to search for products by their key and volume. It performs a search in the loaded dataset and displays the matching products' information.
Profit Calculation: For each matching product, the script calculates the profit by subtracting the cost price from the sell price. It also calculates the profit percentage by dividing the profit by the cost price.
Recommended Prices: The script includes a predefined dictionary of recommended prices for specific products and volumes. It compares the sell price with the recommended prices and calculates the profit and profit percentage based on the recommendations.
Usage
Install the required dependencies by running pip install pandas openpyxl.
Prepare your product data in an Excel file (e.g., Book1.xlsx) with the following columns: Material Code, Material Name, and new price. Ensure that the file is in the same directory as the script.
Run the script and provide the product key and volume when prompted. Enter the sell price for the product.
The script will search for the matching products and display their information, including the cost price, profit, and profit percentage.
If a matching product's key and volume are present in the predefined recommended prices dictionary, the script will also display the recommended price, profit, and profit percentage based on the recommendations.
Repeat steps 3-5 to search for more products, or enter "quit" to exit the script.