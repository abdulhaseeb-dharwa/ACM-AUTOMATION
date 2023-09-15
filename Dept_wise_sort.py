import pandas as pd
import csv 

csv_file = 'Member_list.csv'

converted_data = []

with open(csv_file, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        converted_data.append(row)

columns = ['Timestamp', 'ID', 'Name', 'Departments']

df = pd.DataFrame(converted_data, columns=columns)

df['Departments'] = df['Departments'].str.split(', ')
df = df.explode('Departments')

sorted_df = df.sort_values(by='Departments', ascending=True)

sorted_df.to_csv('sorted_file.csv', index=False)