import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

print("Preview of Data:")
print(df.head())

sales_by_product = df.groupby('Product')['Sales'].sum()

print("\nTotal Sales by Product:")
print(sales_by_product)

sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()
