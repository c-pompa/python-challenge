# Python Challenge - Financial Data & Voter Polling Analysis

## PyBank Assigmment
Created a Python script for analyzing financial records of a company. Given financial data via a .csv. 

To analyze and calculate the results found, the following tasks were performed: 

  - The total number of months included in the dataset
  - The net total amount of "Profit/Losses" over the entire period
  - The average of the changes in "Profit/Losses" over the entire period
  - The greatest increase in profits (date and amount) over the entire period
  - The greatest decrease in losses (date and amount) over the entire period

In addition to the output being printed within the console, the output was also exported to a .txt file found in /analysis/main.txt.

### Challenges - PyBank Assigmment

- During the fist for loop (for row in csvreader), I was having complications finding the changes in Profit/Losses over the entire period. The key word being "changes". I needed to calculate the difference between each row value found under the Profit/Losses column-- while in the for loop. Eventually, I settled with the comprehension formula found on line 31 in main.py. The comprehension subtracts the next row from the current row; all results are put into a list. The value "0" gets added to the beginning of the list as there is no change for the first result. Changes(list) is used to find the average change and combined with bank_dates in order to find the greatest increase and decrease in profits. 

- Printing out the results to the console and .txt file became clustered when .write() and .print() was shown multiple times. To remove cluster, I added ''' (triple apostrophy) to print(f''' text ''') and .write(f''' text'''). 

- Searching through two columns and printing two results did not go smoothly with data_dict. I used zip() instead to combine two lists created from the data and was able to easily search and retreive multiple results from two columns. 


## PyPoll Assignment

Created a Python script that analyzes votes and calculates the following below. The goal is to help a small, rural town modernize its voting process. Provided a .csv data set composed of three columns. 

  - The total number of votes cast
  - A complete list of candidates who received votes
  - The percentage of votes each candidate won
  - The total number of votes each candidate won
  - The winner of the election based on popular vote.

### PyPoll Challenges

  - candidates comprehension list was challenging as I needed to provide a complete list of candidates who received votes. This processes needed to scan the candidates column, find the names of the candidates, ignore listing duplicate named, and provide a count of how many votes each person found received. I used the collections library to assist with created this comprehensions list.

  - A good amount of the code was resued from the PyPoll assignment. While developing the code for the first assignment, the goal was to allow the code to be universal across many projects.


# Acknowledgments

    To the instructors at the USC Data Analyst Bootcamp -- Thanks for the help and guidance!
