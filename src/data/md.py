# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# import dependencies
import pandas as pd


# %%
# load the data
price_data = pd.read_csv('../../data/raw/Bitcoin Historical Data - 07-18-2010_08-18-2020.csv')
price_data


# %%
# set index to date and change its format
price_data = price_data.set_index(price_data['Date'])
price_data.index = pd.to_datetime(price_data.index)
price_data.drop('Date', inplace=True, axis=1)


# %%
price_data


# %%
# price over time
def map_on_price(df):
    df.describe()
    
# merge all google search datasets
def merge_datasets():
    google_search_data = None
    base_path = '../../data/raw/'
    file_names = ['bitcoin-2010_2.csv', 'bitcoin-2011_1.csv', 'bitcoin-2011_2.csv', 'bitcoin-2012_1.csv', 'bitcoin-2012_2.csv',
                'bitcoin-2013_1.csv', 'bitcoin-2013_2.csv', 'bitcoin-2014_1.csv', 'bitcoin-2014_2.csv', 'bitcoin-2015_1.csv',
                'bitcoin-2015_2.csv', 'bitcoin-2016_1.csv', 'bitcoin-2016_2.csv', 'bitcoin-2017_1.csv', 'bitcoin-2017_2.csv',
                'bitcoin-2018_1.csv', 'bitcoin-2018_2.csv', 'bitcoin-2019_1.csv', 'bitcoin-2019_2.csv', 'bitcoin-2020_1.csv',
                'bitcoin-2020_2.csv']
    for file_name in file_names:
        df = pd.read_csv(f'{base_path}{file_name}')
        map_on_price(df)
        if google_search_data is None:
            google_search_data = df
            continue
        google_search_data = pd.concat([google_search_data, df])
    return google_search_data


# %%
merged = merge_datasets()


# %%
merged.columns


# %%
# load google search data
bitcoin_2010_2 = pd.read_csv('../../data/raw/bitcoin-2010_2.csv')
bitcoin_2010_2


# %%
bitcoin_2011_1 = pd.read_csv('../../data/raw/bitcoin-2011_1.csv')
bitcoin_2011_1


# %%
bitcoin_2011_2 = pd.read_csv('../../data/raw/bitcoin-2011_2.csv')
bitcoin_2011_2


# %%
concatenated_temp = pd.concat([bitcoin_2010_2, bitcoin_2011_1, bitcoin_2011_2])
concatenated_temp


# %%
pd.set_option('display.max_rows', None)


# %%
concatenated_temp


# %%



