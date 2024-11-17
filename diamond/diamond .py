# analyze diamonds by cut, color, clarity, price, and other attributes

#  load necessary library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the csv
diamonds_df = pd.read_csv("diamonds.csv")

# Set a seaborn style
sns.set(style="whitegrid")
# 1. Summary statistics of numeric values
print(diamonds_df.describe())

avg_price_by_cut = diamonds_df.groupby('cut')['price'].mean()
print("\nAverage Price by Cut:")
print(avg_price_by_cut)

# 3. Average price by color
avg_price_by_color = diamonds_df.groupby('color')['price'].mean()
print("\nAverage Price by Color:")
print(avg_price_by_color)

# 4. Average price by clarity
avg_price_by_clarity = diamonds_df.groupby('clarity')['price'].mean()
print("\nAverage Price by Clarity:")
print(avg_price_by_clarity)

# 5. Distribution of diamond prices
plt.figure(figsize=(10, 6))
sns.histplot(diamonds_df['price'], bins=50, kde=True, color="blue")
plt.title("Distribution of Diamond Prices", fontsize=16)
plt.xlabel("Price (USD)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

# 6. Average price by cut
plt.figure(figsize=(10, 6))
sns.barplot(x="cut", y="price", data=diamonds_df, ci=None, palette="muted")
plt.title("Average Diamond Price by Cut", fontsize=16)
plt.xlabel("Cut", fontsize=12)
plt.ylabel("Average Price (USD)", fontsize=12)
plt.show()

# 7. Average price by color
plt.figure(figsize=(10, 6))
sns.barplot(x="color", y="price", data=diamonds_df, ci=None, palette="coolwarm")
plt.title("Average Diamond Price by Color", fontsize=16)
plt.xlabel("Color", fontsize=12)
plt.ylabel("Average Price (USD)", fontsize=12)
plt.show()

# 8. Average price by clarity
plt.figure(figsize=(10, 6))
sns.barplot(x="clarity", y="price", data=diamonds_df, ci=None, palette="pastel")
plt.title("Average Diamond Price by Clarity", fontsize=16)
plt.xlabel("Clarity", fontsize=12)
plt.ylabel("Average Price (USD)", fontsize=12)
plt.show()

# 9. Scatter plot of carat vs price
plt.figure(figsize=(10, 6))
sns.scatterplot(x="carat", y="price", hue="cut", data=diamonds_df, palette="deep", alpha=0.6)
plt.title("Carat vs. Price by Cut", fontsize=16)
plt.xlabel("Carat", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)
plt.legend(title="Cut", loc="upper left")
plt.show()
