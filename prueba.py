
import pandas as pd
import numpy as np

### EJERCICIO 0 ###
# print(pd.__version__)

### EJERCICIO 1 ###
# stocks = ['PLW', 'CDR', '11B', 'TEN']
# print(pd.Series(data=stocks))

### EJERCICIO 2 ###
# stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
# quotations = pd.Series(data=stocks)
# print(quotations)

### EJERCICIO 3 ###
# stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
# quotations = pd.Series(data=stocks)
# quotations = quotations.tolist()
# print(quotations)

### EJERCICIO 4 ###
# stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
# quotations = pd.Series(data=stocks)
# quotations = pd.DataFrame(quotations, columns=['price'])
# print(quotations)}

### EJERCICIO 5 ###
# s = pd.Series(
#     data=np.arange(10, 100, 10), 
#     index=np.arange(101, 110), 
#     dtype='float'
# )
# print(s)

### EJERCICIO 6 ###
# series = pd.Series(['001', '002', '003', '004'], list('abcd'))
# series = pd.to_numeric(series)
# print(series)

# series = pd.Series(['001', '002', '003', '004'], list('abcd'))
# series = series.astype(int)
# print(series)


### EJERCICIO 7 ###
# stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
# quotations = pd.Series(data=stocks)
# quotations = quotations.append(pd.Series({'BBT': 25.5, 'F51': 19.2}))
# print(quotations)


### EJERCICIO 8 ###
# stocks = {
#     'PLW': 387.00, 
#     'CDR': 339.5, 
#     'TEN': 349.5, 
#     '11B': 391.0, 
#     'BBT': 25.5, 
#     'F51': 19.2
# }
# quotations = pd.Series(data=stocks)
# quotations_df = quotations.reset_index()
# quotations_df.columns = ['ticker', 'price']
# print(quotations_df)

### EJERCICIO 9 ###
# data_dict = {'company': ['Amazon', 'Microsoft', 'Facebook'],
# 'price': [2375.0, 178.6, 179.2],
# 'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']}
# companies = pd.DataFrame(data=data_dict)
# print(companies)

### EJERCICIO 10 ###
# data_dict = {
#     'company': ['Amazon', 'Microsoft', 'Facebook'],
#     'price': [2375.00, 178.6, 179.2],
#     'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']
# }
# companies = pd.DataFrame(data=data_dict)
# companies = companies.set_index('company')
# print(companies)

### EJERCICIO 11 ###
# date_range = pd.date_range(start='2020-01-01', periods=31)
# print(date_range)
# DatetimeIndex = pd.date_range(start='2020/1/1', end='2020/1/31')
# print(DatetimeIndex)

### EJERCICIO 12 ###
# date_range = pd.date_range(start='2020-01-01', periods=52, freq='W-MON')
# print(date_range)
# Date_Range = pd.date_range( start='2020/1/6', end='2020/12/31', freq='W-MON')
# print(Date_Range)

### EJERCICIO 13 ###
# date_range = pd.date_range(
#     start='2021-01-01', 
#     end='2021-01-02', 
#     freq='H', 
#     closed='left'
# )
# print(date_range)
# Date_Range = pd.date_range( start='2021/1/1', end='2021/1/1 23:00:00', freq='H')
# print(Date_Range)
# date_range = pd.date_range(start='2021-01-01', periods=24, freq='H')
# print(date_range)

### EJERCICIO 14 ###
date_range = pd.date_range(start='2021-03-01', periods=31)
df = pd.DataFrame(data=date_range, columns=['day'])
df['day_of_year'] = df['day'].dt.dayofyear
print(df)
date_range = pd.date_range(start='2021/3/1',  end='2021/3/31')
df = pd.DataFrame(data=date_range, columns=['day'])
df['day_of_year'] = df['day'].dt.dayofyear
print(df)

### EJERCICIO 15 ###
### EJERCICIO 16 ###
