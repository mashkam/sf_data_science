import pandas as pd

melb_df = pd.read_csv('data/melb_data_fe.csv')
print(melb_df.head())
print(melb_df.info)

melb_df['Date'] = pd.to_datetime(melb_df['Date'])
quarters = melb_df['Date'].dt.quarter
print(quarters.value_counts().iloc[1])

cols_to_exclude = ['Date', 'Rooms', 'Bathroom', 'Bedroom', 'Car']
max_unique_count = 150
for col in melb_df.columns:
    if melb_df[col].nunique(
    ) < max_unique_count and col not in cols_to_exclude:
        melb_df[col] = melb_df[col].astype('category')
print(melb_df.info)

print(round(melb_df.sort_values(by='AreaRatio', ignore_index=True,
                                ascending=False).loc[1558, 'BuildingArea']))

mask1 = melb_df['Type'] == 'townhouse'
mask2 = melb_df['Rooms'] > 2
print(round(melb_df[mask1 & mask2].sort_values(
    by=['Rooms', 'MeanRoomsSquare'], ascending=[
        True, False], ignore_index=True).loc[18, 'Price']))

print(melb_df.groupby('Rooms')['Price'].mean().sort_values(ascending=False))

print(melb_df.groupby('Regionname')['Lattitude'].std().sort_values())

date1 = pd.to_datetime('2017-05-01')
date2 = pd.to_datetime('2017-09-01')
mask = (date1 <= melb_df['Date']) & (melb_df['Date'] <= date2)
print(melb_df.groupby('SellerG')['Price'].sum().sort_values(ascending=True))

pivot = melb_df.pivot_table(
    values='Price',
    index='SellerG',
    columns='Type',
    aggfunc='mean',
    fill_value=0
)
max_unit_price = pivot['unit'].max()
print(pivot[pivot['unit'] == max_unit_price].index[0])
