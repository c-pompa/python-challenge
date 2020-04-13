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
        changes.insert(0, 0)
        avg_change = round(sum(changes) / total_months, 2)

        data_dict = {"Date": bank_dates, "Profit/Losses": pandl_list, "Difference": changes}
        
  
    #make index as values for dict rows / not used
    #res = dict(zip(changes, range(2, len(changes)+1))) 
    # Zip: Combing two lists to iterate through
    search = zip(bank_dates, (changes))

    # The greatest increase in profits (date and amount) over the entire period
    # Iterate through conbined lists
    for row in search:
        if row[1] == max(data_dict["Difference"]):
            increase = row[1]
            increase_date = row[0]
            break
            #print(f"Greatest Increase in Profits: {row[0]} ${row[1]}")

    # The greatest decrease in losses (date and amount) over the entire period      
    for rowmin in search:
        if rowmin[1] == min(data_dict["Difference"]):
            decrease = rowmin[1]
            decrease_date = rowmin[0]
            break
            #print(f"Greatest Increase in Profits: {rowmin[0]} ${rowmin[1]}")

    # Export a text file with the results
    file1 = open("main.txt","w")
    file1.write("Financial Analysis\n") 
    file1.write("----------------------------\n") 
    file1.write(f"Total Months: {total_months}\n") 
    file1.write(f"Total: ${sum_months}\n") 
    file1.write(f"Average  Change: ${avg_change}\n") 
    file1.write(f"Greatest Increase in Profits: {row[0]} ${row[1]}\n") 
    file1.write(f"Greatest Decrease in Profits: {rowmin[0]} ${rowmin[1]}\n") 
    file1.close() 

    # Export results to terminal
    print("Financial Analysis") 
    print("----------------------------") 
    print(f"Total Months: {total_months}")
    print(f"Total: ${sum_months}")
    print(f"Average  Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {row[0]} ${row[1]}")
    print(f"Greatest Decrease in Profits: {rowmin[0]} ${rowmin[1]}")
