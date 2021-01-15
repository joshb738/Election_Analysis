# Add dependencies
import csv
import os

# Assign variable to load the file from a path.
file_to_load = os.path.join("resources", "election_results.csv")

# Assign Variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total vote counter
total_votes = 0

# Create candidate options list
candidate_options = []

# Decalare the empty dictionary
candidate_votes = {}    

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# read and print header row.
    headers = next(file_reader)
  
    # Print each row in the CSV file.
    for row in file_reader:
        # Increment the total votes after the for loop
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match the existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Track the candidates vote count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidates count.
        candidate_votes[candidate_name] += 1

#Save the results to text file
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate 
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        # Determine winning candidate, vote percentage and count
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their percentage and count to the terminal
        print(candidate_results)
        # Save the cadidate results to the text file
        txt_file.write(candidate_results + "\n")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidate results to text file
    txt_file.write(winning_candidate_summary)
