import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

frequency_table = car_eval['manufacturer_country'].value_counts()
print(frequency_table)

fourth_most_common_country = frequency_table.index[3]
print("Country 4th Most Frequently:", fourth_most_common_country)

proportion_table = car_eval['manufacturer_country'].value_counts(normalize=True) * 100
percentage_japan = proportion_table.get('Japan', 0) 
print("Percentage of Cars Manufactured in Japan:", percentage_japan)

buying_cost_values = car_eval['buying_cost'].unique()
print("Possible values of buying_cost:", buying_cost_values)

buying_cost_categories = sorted(car_eval['buying_cost'].unique())
print("Ordered buying_cost categories:", buying_cost_categories)

car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], categories=buying_cost_categories, ordered=True)
print(car_eval.head())

median_category_num = np.median(car_eval['buying_cost'].cat.codes)
print(median_category_num) 
median_category = int(median_category_num)
print(median_category)

proportion_table_with_missing = count_table_with_missing = car_eval['luggage'].value_counts(dropna=False)
print(proportion_table_with_missing)

count_5_or_more_doors = car_eval[car_eval['doors'] == '5more'].shape[0]
print("Count of cars with 5 or more doors:", count_5_or_more_doors)

proportion_5_or_more_doors = car_eval[car_eval['doors'] == '5more'].shape[0] / len(car_eval) * 100
print("Proportion of cars with 5 or more doors:", proportion_5_or_more_doors)