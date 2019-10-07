import pandas as pd 
import os

# get the data and transfer it to a pandas dataframe
filepath = os.path.join("PyPoll","election_data.csv")

election_data = pd.read_csv(filepath)

# total votes
total_votes = len(election_data)
print(election_data.head())