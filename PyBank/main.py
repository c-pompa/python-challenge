# * Your task is to create a Python script that analyzes the records to calculate each of the following:

import csv
import numpy as np
import pandas as pd

reader = pd.read_csv('C:\\Users\\pompa\\gitProjects\\python-challenge\\PyBank\\Resources\\budget_data.csv', skiprows=0)
# print(reader)

df_data = pd.DataFrame(reader)
# print(df_data['Date'])


#   * The total number of months included in the dataset
total_months = len(df_data['Date'])
print(f"Total Months: {total_months}")


#   * The net total amount of "Profit/Losses" over the entire period
total_pl = sum(df_data['Profit/Losses'])
print(f"Total: ${total_pl}")

#   * The average of the changes in "Profit/Losses" over the entire period

data_pl = df_data['Profit/Losses'].diff()
data_pl_avg = round((data_pl.sum() / total_months), 2)
print(f"Average Change: ${data_pl_avg}")


#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
# 