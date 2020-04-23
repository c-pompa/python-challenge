# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
import csv
import pathlib
import collections

# Give a path to the csvfile
csvpath = pathlib.Path('C:\\Users\\pompa\\gitProjects\\python-challenge\\PyPoll\\Resources\\election_data.csv')

candidates_list = []
# Open the csv file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # The total number of all votes received
    total_votes = 0
    for row in csvreader:
        candidates_list.append(row[2])
        total_votes += 1

    # A complete list of candidates who received votes
    candidates = [item for item, count in collections.Counter(candidates_list).items() if count > 1]

    # The percentage of votes each candidate won
    candidate = {}
    percentage = {}
    # Loop through candidates list and return candidate with count value and 
    # percentage of votes acquired to total vote
    for i in candidates:
        candidate[i] = candidates_list.count(i)
        percentage[i] =  round(candidates_list.count(i) / total_votes * 100, 3)
        #candidate[i] = percentage[i], candidates_list.count(i)
    
    # Search through candidates with max votes. Return the winner.
    winner_values = max(candidate.values())
    winner = [k for k, v in candidate.items() if v == winner_values]

# Export a text file with the results
pypoll_txt = open("./analysis/main.txt","w")
pypoll_txt.write(
f'''
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
{candidates[0]}: {percentage[candidates[0]]}% ({candidate[candidates[0]]})
{candidates[1]}: {percentage[candidates[1]]}% ({candidate[candidates[1]]})
{candidates[2]}: {percentage[candidates[2]]}% ({candidate[candidates[2]]})
{candidates[3]}: {percentage[candidates[3]]}% ({candidate[candidates[3]]})
----------------------------
Winner: {winner[0]}
----------------------------''')
pypoll_txt.close() 

# # Export results to terminal
print(
f'''
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
{candidates[0]}: {percentage[candidates[0]]}% ({candidate[candidates[0]]})
{candidates[1]}: {percentage[candidates[1]]}% ({candidate[candidates[1]]})
{candidates[2]}: {percentage[candidates[2]]}% ({candidate[candidates[2]]})
{candidates[3]}: {percentage[candidates[3]]}% ({candidate[candidates[3]]})
----------------------------
Winner: {winner[0]}
----------------------------''')