import pandas as pd 
import os

# get the data and transfer it to a pandas dataframe
filepath = os.path.join("PyPoll","election_data.csv")
election_data = pd.read_csv(filepath)

# total votes of all the candidates
total_votes = len(election_data)

#convert the candidate list into a set to filter the unique candidates' names for following analysis
candidate_set = set(election_data["Candidate"])

# convert the set to a list again for further analysis
candidate_list = list(candidate_set)

print(f'Election Results\n----------------------------')

# write results in file, create a new file in the same directory
results = open("PyPoll\\Election_Results.txt","w")
results.write(f'Election Results\n----------------------------\n')

# variable to compare percentage amoung candidates
p = 0

# for loop to analyze each candidate in the list, and print info for each candidate 
# as well as to write the results into the text file
for i in range(len(candidate_list)):
    candidate = election_data["Candidate"][election_data["Candidate"]==candidate_list[i]] # filter out the votes of unique candidate and store it as a list
    total_candidate_votes = len(candidate) # get the total votes of this candidate
    percent = total_candidate_votes/total_votes*100 # calculate the percentage of the vote this candidate got
    if percent > p:   # if statement to find the higher voted candidate and his/her name
        p = percent
        candidate_name = candidate_list[i]
    print(f'{candidate_list[i]}: {percent:.3f}% ({total_candidate_votes})')
    results.write(f'{candidate_list[i]}: {percent:.3f}% ({total_candidate_votes})\n')
print(f'----------------------------')
print(f'Winner: {candidate_name}')
results.write(f'----------------------------\n')
results.write(f'Winner: {candidate_name}\n')

# close file
results.close()