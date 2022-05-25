import pandas as pd

melb_data = pd.read_csv('data/melb_data_ps.csv', sep=',')
print(melb_data.head())

melb_df = melb_data.copy()
print(melb_df.head())

melb_df['Date'] = pd.to_datetime(melb_df['Date'])
print(melb_df['Date'])

melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale']
                                                         == 6)].shape[0]
print(weekend_count)


def get_weekend(weekday):
    if weekday == 5 or weekday == 6:
        return 1
    else:
        return 0


melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
print(round(melb_df[melb_df['Weekend'] == 1]['Price'].mean(), 2))

popular_seler = melb_df['SellerG'].value_counts().nlargest(49).index
melb_df['SellerG'] = melb_df['SellerG'].apply(
    lambda x: x if x in popular_seler else 'other')
a = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min()
b = melb_df[melb_df['SellerG'] == 'other']['Price'].min()
print(round(a / b, 1))

print(melb_df.info())
popular_suburb = melb_df['Suburb'].value_counts().nlargest(119).index
melb_df['Suburb'] = melb_df['Suburb'].apply(
    lambda x: x if x in popular_suburb else 'other')
melb_df['Suburb'] = melb_df['Suburb'].astype('category')
print(melb_df.info())
