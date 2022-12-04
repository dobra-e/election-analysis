# Election Analysis
## Project Overview
Voters in a local congressional precinct cast their ballots by mail, punch cards, or direct recording electronic (DRE) counting machines. Votes are counted at the central office and the results are certified. A Colorado Board of Elections employee asked for an election audit of a recent local congressional election. The report must include: 
* the total number of votes cast
* the number and percentage of votes by county
* the county with the highest voter turnout
* a complete list of candidates who received votes
* the total number and percentage of votes by candidate
* the winner of the election based on popular vote

### Purpose
The purpose of this project is to create an automated process to audit a local congressional election that can be applied to future congressional, senatorial, and local elections. A vote count report must be generated to certify the results of the election.

## Resources
- Data source: election_results.csv
- Software: Python 3.9.12, Visual Studio Code 1.73.1

## Results
### The Code
The code utilized arrays, dictionaries, `for` loops, conditional statements, and f-strings to produce the output. 

#### Total Votes
First, `total_votes` was initialize and set to zero to store the vote count. Then, within a `for` loop, `total_votes` was increased by one for each row in the file:
```
for row in reader:
  total_votes = total + 1
```

#### County Results
An empty array and dictionary, `county_list` and `county_votes`, respectively, were created. 
```
county_list = []
county_votes = {}
```
Then, within the same `for` loop, the county name was extracted from each row in the file. 
```
county_name = row[1]
```
If the name was not already in `county_list`, it was appended. The votes per county was then tracked and increased by one for each row.
```
if county_name not in county_list:
  county_list.append(county_name)
  county_votes[county_name] = 0
county_votes[county_name] += 1
```
`largest_turnout` and `largest_votecount` were initialized earlier in the script. Another `for` loop was then used to retreive the county from the dictionary, the vote count per county, percentage of votes per county, and the county with largest turnout. 
```
largest_turnout = ""
largest_votecount = 0
# ...
for county_name in county_list:
  votesCount = county_votes.get(county_name)
  votesCount_percentage = float(votesCount)/float(total_votes)*100
  
  if (votesCount > largest_votecount):
    largest_votecount = votesCount
    largest_turnout = county_name
```
#### Saving to a Text File
To write the results to a text file, a file was opened and a variable was created to hold f-strings with the results. For example: 
```
file_to_save = os.path.join("analysis", "election_analysis.txt")
# ...
with open(file_to_save, "w") as txt_file:
  # ...
  county_results=(f"{county_name}: {votesCount_percentage:.1f}% ({votesCount:,})\n")
  txt_file.write(county_results)
```
The same method was used to produce the candidate results. 

### The Output
The analysis of the election shows that:
- There were 369,711 votes cast in the congressional election.
- The county results were:
  - Jefferson County cast 10.5% or 38,855 of the total votes.
  - Denver County cast 82.8% or 306,055 of the total votes.
  - Arapahoe County cast 6.7% or 24,801 of the total votes.
  - The county with the largest voter turnout was Denver.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  -  Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
  -  Diana DeGette received 73.8% of the vote with 272,892 votes.
  -  Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote with 272,892 votes.

## Summary
The audit of the Colorado congressional race was successfully completed using the automated python script. The script looped through each row to extract the county names, candidate names, and tabulate the number of votes for each as well as write the results to a text file. 

With minor adjustments, the script could be applied to any election. Some of the adjustments may include updating the: 
* file path to a different csv of election data
* indexed columns to match the new dataset
* variable names to match the new dataset
* f-string text to reflect the specifics of the election 

### File Path
The file path in the script would need to be updated to point to the new elections data file. For example, "Resources" would need to be changed to the correct folder name that holds the data file and "election_results.csv" would need to be updated to reflect the name of the data file.
```
file_to_load = os.path.join("Resources", "election_results.csv")
```

### Indexed Columns
Within the first `for` loop, the indexed column may need to be updated to match the location of the correct columns in the data file. For instance, if candidate names were listed in column 4 instead of column 3, the code would read:
```
for row in reader:
  candidate_name = row[3]
```

### Variable Names
If state election results opposed to county results were analyzed, variable names could be updated to match. For instance, `county_votes` could be updated to `state_votes`. Another option would be to use a more universal variable name such as `votingBlock_votes` for all elections.

### F-string Text
Finally, some of the f-string text output may need to be updated to reflect the characteristics of the election. For example, "Largest County Turnout" may need to be updated to "Largest District Turnout" for smaller, local elections.
```
largest_county_turnout = (f"Largest County Turnout: {largest_turnout}\n")
```
