sales_data = {
"Product A": [100, 200, 150],
"Product B": [50, 75, 100],
"Product C": [300, 250, 400]
}
total_sales= {}
for product,sales in sales_data.items():
    total_sales[product]= sum(sales)
print(total_sales)