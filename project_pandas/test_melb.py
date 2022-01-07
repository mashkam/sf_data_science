import os
import pandas as pd
import os.path as op
import urllib.request
import zipfile
import numpy as np


# create data dir
data_path = 'data'  # op.join(op.dirname(op.realpath(__file__)), 'data')
os.makedirs(data_path, exist_ok=True)

if not op.exists(op.join(data_path, 'countries.csv')):
    countries_df = pd.DataFrame({
        'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь',
                    'Казахстан'],
        'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
        'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
    })

    countries_df.to_csv(op.join(data_path, 'countries.csv'),
                        index=False,
                        sep=';')

melb_data_path = op.join(data_path, 'melb_data.csv')
if not op.exists(melb_data_path):
    url = 'https://lms.skillfactory.ru/assets/courseware/v1/' \
          'a37d26d144a33e5bc8a1ac9aa5679cf8/asset-v1:' \
          'SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/melb_data.zip'
    filehandle, _ = urllib.request.urlretrieve(url)
    zip_file_object = zipfile.ZipFile(filehandle, 'r')
    file = zip_file_object.extract(op.basename(melb_data_path), path=data_path)

melb_data = pd.read_csv(melb_data_path, sep=',')

print("5.1 Answer:", melb_data.loc[15].Price)

print("5.2 Answer:", melb_data.loc[90].Date)

print("5.3 Answer:",
      round(melb_data.loc[3521].Landsize / melb_data.loc[1690].Landsize))

print("6.3 Answer:", melb_data["Coordinates"].dtype)

print("6.5 Answer:", melb_data.CouncilArea.isnull().sum())

melb_data['Postcode'] = melb_data['Postcode'].astype(np.int64)
melb_data['Car'] = melb_data['Car'].astype(np.int64)
melb_data['Bedroom'] = melb_data['Bedroom'].astype(np.int64)
melb_data['Bathroom'] = melb_data['Bathroom'].astype(np.int64)
melb_data['Propertycount'] = melb_data['Propertycount'].astype(np.int64)
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype(np.int64)
print(melb_data.info())

print(melb_data['Type'].value_counts(normalize=True))

print(round(melb_data['Distance'].std()))

building_median = melb_data['BuildingArea'].median()
building_mean = melb_data['BuildingArea'].mean()
deviance = abs(building_median - building_mean) / building_mean
print(round(deviance * 100))

print(melb_data['Bedroom'].mode())

print(melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3e6)
                ].shape[0])

print(melb_data[melb_data['BuildingArea'] == 0]['Price'].min())

print(round(melb_data[(melb_data['Price'] < 1e6) & ((melb_data['Bedroom'] > 5)
            | (melb_data['YearBuilt'] > 2015))]['Price'].mean()))

print(melb_data[(melb_data['Type'] == 'h') & (melb_data['Price'] < 3e6)]
      ['Regionname'].mode())
