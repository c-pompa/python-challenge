# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Export a text file with the results
pypoll_txt = open("main.txt","w")
pypoll_txt.write(
f'''
Election Results
----------------------------
Total Votes: {total_months}
----------------------------
Name: PERCENTAGE (# OF VOTES)
Name: PERCENTAGE (# OF VOTES)
Name: PERCENTAGE (# OF VOTES)
Name: PERCENTAGE (# OF VOTES)
----------------------------
Winner: NAME
----------------------------
''')
pypoll_txt.close() 

# # Export results to terminal
print(
f'''
Election Results
----------------------------
Total Votes: {total_months}
----------------------------
Name: PERCENTAGE (# OF VOTES)
Name: PERCENTAGE (# OF VOTES)
Name: PERCENTAGE (# OF VOTES)
Name: PERCENTAGE (# OF VOTES)
----------------------------
Winner: NAME
----------------------------
''')
