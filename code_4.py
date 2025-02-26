import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)
#import datetime as day

def get_big_mac_price_by_year(year,country_code):
    
    country = country_code.upper()
    
    if type(year) == int:
        year = str(year)
        
    cntry_df = df[df['iso_a3'] == country]
    
    total = 0
    
    for i in cntry_df.index: #using df.index iteration
        row = cntry_df['date'][i]
        if row[:4] == year:
            total += cntry_df['dollar_price'][i]
    
    return round(total.mean(),2)

    #year_date = day.datetime.year()
    #split_date = df['date']
    #yr = df[]
    #pass
    #quer = f"(iso_a3 == country_code and 'date' == year)"
    #country_df = df.query(quer)
    #return round(country_df['dollar_price'].mean(),2) #this rounds to 2 decimals

def get_big_mac_price_by_country(country_code):
    
    country = country_code.upper()
    #this creates a data frame that only contains the rows with a matching country code
    cntry_df = df[df['iso_a3'] == country]
    cnt = 0
    
    for i in cntry_df.index: #using df.index iteration
        cnt +=1
    print(cnt)     
    return round(cntry_df['dollar_price'].mean(),2)

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    #pass # Remove this line and code your user interface
    avg = get_big_mac_price_by_year(2000,'ARG')
    print(avg)
    
    mean_price = get_big_mac_price_by_country('arg')
    print(mean_price)
    