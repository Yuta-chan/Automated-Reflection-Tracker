import os
import re
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

def next_number():
    max_number = 0
    pattern = r'evaluation_v(\d+)\.csv'

    for file in os.listdir('./files'):
        match = re.match(pattern, file)
        if match:
            number = int(match.group(1))
            max_number = max(max_number, number)
    
    return max_number + 1

response = input("Do you want to start a new document? (y/n): ").lower()
if response == 'y':
    file_number = next_number()
    file_name = f'files/evaluation_v{file_number}.csv'

    with open(file_name, 'w', newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL) 

        while True:
            print("Instructions:\nTo finish, type -1 in any question and Press Enter")

            field = input("What do you want to evaluate?: ")
            if field == "-1":
                break
            feeling = input("How do you really feel about what you are evaluating?\n On a scale from 0 (the worst) to 10 (the most enjoyable): ")
            impact = input("How impactful is what you are evaluating in your life?\n On a scale from 0 (almost nothing) to 10 (a lot, almost every day): ")
            note = input("Is there anything remarkable you want to add about what you are evaluating?\n If not, just press Enter\n")
            date = datetime.date.today().strftime('%Y-%m-%d')
            # date = input(f"Date of the record in 'yyyy-mm-dd' (default: {today_date}): ") or today_date

            w.writerow([field, feeling, impact, note, date]) 

def last_file():
    files = [file for file in os.listdir('./files') if re.match(r'evaluation_v\d+\.csv', file)]
    if files:
        # Separate lambda expression out of the f-string
        sorted_files = sorted(files, key=lambda x: int(re.findall(r'(\d+)', x)[0]))
        return f"./files/{sorted_files[-1]}"
    else:
        return f'./files/evaluation_v1.csv'

file_name = last_file()

# Use the last_file function to get the latest file
file_name = last_file()

# Column names you want to assign to the DataFrame
column_names = ['Field', 'Feeling', 'Impact', 'Note', 'Date']

# Read the data from the CSV file
df = pd.read_csv(file_name, names=column_names, header=None)
# Fill empty fields with "NA"
df.fillna("NA", inplace=True)

# Set display options
pd.set_option('display.max_rows', None)       # If you want to see all rows
pd.set_option('display.max_columns', None)    # If you want to see all columns
pd.set_option('display.width', None)          # Adjust the width to avoid cutting columns
pd.set_option('display.max_colwidth', None)   # To see the full content of the columns

# Display the DataFrame in the terminal in a nice way
print('\n')
print(df.to_string(index=False))
print('\n')

