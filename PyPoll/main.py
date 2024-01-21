import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

Total_Votes = 0
Candidate_Votes = {}

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        Total_Votes += 1
        Candidate_Name = row[2]

        if Candidate_Name in Candidate_Votes:
            Candidate_Votes[Candidate_Name] += 1
        else:
            Candidate_Votes[Candidate_Name] = 1

Candidates_Percentage = {Candidate: (Votes / Total_Votes) * 100 for Candidate, Votes in Candidate_Votes.items()}

Winner = max(Candidate_Votes, key=Candidate_Votes.get)

Election_Results = {
    "Total_Votes": Total_Votes,
    "Candidate_Votes": Candidate_Votes,
    "Candidate_Percentage": Candidates_Percentage,
    "Winner": Winner
}

print("Election Results")
print("----------------------------")
print(f"Total Votes: {Total_Votes}")
print("----------------------------")
for Candidate, Votes in Election_Results['Candidate_Votes'].items():
    percentage = Election_Results['Candidate_Percentage'][Candidate]
    print(f"{Candidate}: {percentage:.3f}% ({Votes})")
print("----------------------------")
print(f"Winner: {Winner}")
(f"Winner: {Winner}")

output_file = os.path.join("Analysis", "PyPoll Analysis.txt")

with open(output_file, "w", newline='') as datafile:
    datafile.write("Election Results\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Votes: {Total_Votes}\n")
    for Candidate, Votes in Election_Results['Candidate_Votes'].items():
        percentage = Election_Results['Candidate_Percentage'][Candidate]
        datafile.write(f"{Candidate}: {percentage:.3f}% ({Votes})\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Winner: {Winner}\n")
    datafile.write("----------------------------\n")

print(f"Results exported to: {output_file}")















