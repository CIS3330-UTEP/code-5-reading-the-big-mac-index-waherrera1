import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

#this function solves the problem by creating a dataframe that only includes the rows
# with the same country code
#it then uses iterrows to iterate through the data frame and add the dollar_price 
# of the rows with the same year, and finally returns the average of this sum

def get_big_mac_price_by_year(year,country_code):
    
    if type(year) == int:
        year = str(year)
    
    country = country_code.upper()  
    cntry_df = df[df['iso_a3'] == country]
    total = 0
    
    for index, row in cntry_df.iterrows(): 
        if row['date'][:4] == year:
            total += cntry_df['dollar_price'][index] 
    
    # for i in cntry_df.index: #using df.index iteration
    #     row = cntry_df['date'][i] #getting the string of the row under the column 'date'
    #     if row[:4] == year:
    #         total += cntry_df['dollar_price'][i]
            
    return round(total.mean(),2)

#this function solves the problem by creating a data frame that contains the rows 
# under the column with a matching country code
def get_big_mac_price_by_country(country_code):
    
    country = country_code.upper()
    cntry_df = df[df['iso_a3'] == country]  
    return round(cntry_df['dollar_price'].mean(),2) 

#this function
def get_the_cheapest_big_mac_price_by_year(year):
    
    if type(year) == int:
        year = str(year)
    
    #temporary variable values
    min = 9999 
    country_name = None
    country_code = None
    dollar_price = None
    
    for index, row in df.iterrows():
        if row['dollar_price'] < min and row['date'][:4] == year:
            min = df['dollar_price'][index]
            dollar_price = round(min,2)
            country_code = df['currency_code'][index]
            country_name = df['name'][index]

    return f'{country_name}({country_code}): ${dollar_price}'

def get_the_most_expensive_big_mac_price_by_year(year):

    if type(year) == int:
        year = str(year)
    
    #temporary values for variables
    max = 0 
    country_name = None
    country_code = None
    dollar_price = None
    
    for index, row in df.iterrows():
        if row['dollar_price'] > max and row['date'][:4] == year:
            max = df['dollar_price'][index]
            dollar_price = round(max,2)
            country_code = df['currency_code'][index]
            country_name = df['name'][index]
             
    return f'{country_name}({country_code}): ${dollar_price}'

if __name__ == "__main__":
    #pass # Remove this line and code your user interface
    avg = get_big_mac_price_by_year(2000,'ARG')
    #print(avg)
    
    mean_price = get_big_mac_price_by_country('arg')
    #print(mean_price)
    
    cheap_yr = get_the_cheapest_big_mac_price_by_year(2008)
    print(cheap_yr)
    
    pricey_yr = get_the_most_expensive_big_mac_price_by_year(2003)
    print(pricey_yr)
    