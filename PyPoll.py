# dependencies
import csv
import os

# assign variable to load a file
file_to_load = os.path.join("Resources", "election_results.csv")

# assign variable to save a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter 
total_votes = 0

# declare a list of candidate options
candidate_options = []

# votes dictionary
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read and print the header row
    headers = next(file_reader)

    # print each row of the csv file
    for row in file_reader:
        # add to the total vote counter
        total_votes += 1

        # get candidate name for each row
        candidate_name = row[2]

        # check if candidate name exists in list
        if candidate_name not in candidate_options:
            # add to list
            candidate_options.append(candidate_name)
            # track candidates vote count
            candidate_votes[candidate_name] = 0
        
        # add votes to each candidates vote count
        candidate_votes[candidate_name] += 1

# save results to text file
with open(file_to_save, "w") as txt_file:
    # print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n")
    print(election_results, end="")
    # save the final vote count to the text file
    txt_file.write(election_results)

    # determine percentage of votes for each candidate
    # iterate through the candidate list
    for candidate_name in candidate_votes:
        # retrieve vote count for candidate
        votes = candidate_votes[candidate_name]
        # calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # print candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # save candidate results to the text file
        txt_file.write(candidate_results)

        # determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes an winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # set winning_candidate = candidate's name
            winning_candidate = candidate_name
        
    # print winning candidate summary
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")
    print(winning_candidate_summary)
    # save winning candidate summary to text file
    txt_file.write(winning_candidate_summary)