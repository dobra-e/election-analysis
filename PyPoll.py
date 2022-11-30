# Data we need to retrieve
# 1. the total number of votes cast
# 2. a complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote

# dependencies
import csv
import os

# assign variable to load a file
file_to_load = os.path.join("Resources", "election_results.csv")

# assign variable to save a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file
with open(file_to_load) as election_data:

    # read the file
    file_reader = csv.reader(election_data)

    # print the header row
    headers = next(file_reader)
    print(headers)

  





