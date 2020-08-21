import pandas as pd                        
from pytrends.request import TrendReq
from pytrends import dailydata
import time
from collections import defaultdict

def load_keywords(fname):
    ''' Load the file using std open'''
    keywords = []
    f = open(fname,'r')
    for line in f.readlines():
        keywords.append(line.strip())
    f.close()
    return keywords

def fetch():
    pytrend = TrendReq(hl='en-GB', tz=360) 
    keywords_list = load_keywords("./data/raw/keywords_list.txt")
    data = defaultdict(list)
    for x in range(0,len(keywords_list)): 
        keyword = keywords_list[x]
        df = dailydata.get_daily_data(keyword, 2004, 8, 2020, 8, geo = 'GB')
        if not df.empty: 
            col_name = f'{keyword}_unscaled'
            values = list(df[col_name].values)
            data[keyword] = values

    data_by_days = pd.DataFrame.from_dict(data)
    data_by_days = data_by_days.set_index(df.index)
    data_by_days.to_csv('./data/raw/search_trends.csv') 
    print('Data is fetched!')

def main():
    ''' Connects to google api to scrape trends data'''
    fetch()

if __name__ == '__main__':
    main()


# 