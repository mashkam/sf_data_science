import pandas as pd

orders_df = pd.read_csv('data/orders_and_products/orders.csv', sep=';')
products_df = pd.read_csv('data/orders_and_products/products.csv', sep=';')

orders_products = orders_df.merge(
    products_df,
    left_on='ID товара',
    right_on='Product_ID',
    how='left')

print("8.8:", orders_products[orders_products['Product_ID'].isnull()]
      .iloc[0]['Order ID'])

print("8.9:", orders_products[orders_products['Отменен'] == 'Да']['Name'])

orders_products['Profit'] = orders_products['Price'] * orders_products[
    'Количество']
print(orders_products[orders_products['Оплачен'] == 'Да'].groupby(
    'ID Покупателя')['Profit'].sum().sort_values(ascending=False))
