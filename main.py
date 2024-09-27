import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Read the cart data
df = pd.read_csv('2024-09-16T091030.csv')

# Extract item names and prices
items = df['Description']
prices = df['Unit Price'] * df['Quantity']

# Create the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=prices, label=items, alpha=.8)
plt.title('Digikey Cart Treemap')
plt.axis('off')
plt.show()
