# * Your task is to create a Python script that analyzes the records to calculate each of the following:

import csv
import pathlib

csvpath = pathlib.Path('C:\\Users\\pompa\\gitProjects\\python-challenge\\PyBank\\Resources\\budget_data.csv')

bank_list = []
pandl_list = []
pandl_changes = []
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # The total number of months included in the dataset
    bank_dates = []
    total_months = 0
    sum_months = 0

    for row in csvreader:
        bank_dates.append(row[0])
        total_months += 1
        # The net total amount of "Profit/Losses" over the entire period
        sum_months += int(row[1])
        # make a list with Profit/Losses column values
        pandl_list.append(int(row[1]))
        # The average of the changes in "Profit/Losses" over the entire period                               
        changes = [pandl_list[i + 1] - pandl_list[i] for i in range(len(pandl_list)-1)]
          #  pandl_changes.append(changes)
        avg_change = round(sum(changes) / total_months, 2)

        data_dict = {"Date": bank_dates, "Profit/Losses": pandl_list, "Difference": changes}
        

        key = list(data_dict.values())
        #key2 = max(key)

            
        # temp_dict = {}
        # for key, value in data_dict.items():

        #     if value == 10000:
        #         temp_dict[key] = value
        #     else:
        #         print("doesnt work")
        #     break


        #maxChanges_list = max(data_dict["Difference"])
        #maxChange = (maxChanges_list)

    # Another option to run the for loop involves Python's enumerate method
    #This method obtains both the index and the value of an item during a for loop
       
        

    # print(max(maxChanges))

    print("Financial Analysis") 
    print("----------------------------") 
    print(f"Total Months: {total_months}")
    print(f"Total: ${sum_months}")
    print(f"Average  Change: ${avg_change}")
    print(data_dict["Difference"])
    #print(f"Greatest Increase in Profits: ${max(maxChanges)}")



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
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
