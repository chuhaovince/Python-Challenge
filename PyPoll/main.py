import pandas as pd 
import os

# get the data and transfer it to a pandas dataframe
filepath = os.path.join("PyPoll","election_data.csv")

election_data = pd.read_csv(filepath)

# total votes
total_votes = len(election_data)

#convert the candidate list into a set so i can know the candidates' names for following analysis
candidate_set = set(election_data["Candidate"])

# convert the set to a list again so i have a list of all unique names
candidate_list = list(candidate_set)

print(f'Election Results\n-----------------------')

# write results in file, create a new file in the same directory
results = open("PyPoll\Election_Results.txt","w")
results.write(f'Election Results\n-----------------------\n')

#variable to compare percentage amoung candidates
p = 0
for i in range(len(candidate_list)):
    candidate = election_data["Candidate"][election_data["Candidate"]==candidate_list[i]]
    total_candidate_votes = len(candidate)
    percent = total_candidate_votes/total_votes*100
    if percent > p:
        p = percent
        candidate_name = candidate_list[i]
    print(f'{candidate_list[i]}: {percent:.3f}% ({total_candidate_votes})')
    results.write(f'{candidate_list[i]}: {percent:.3f}% ({total_candidate_votes})\n')
print(f'-----------------------')
print(f'Winner: {candidate_name}')
results.write(f'-----------------------\n')
results.write(f'Winner: {candidate_name}\n')

results.close()