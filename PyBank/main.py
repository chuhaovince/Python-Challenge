# import modules in python
import pandas as pd
import os

# Open pybank csv file with pandas dataframe
filepath = os.path.join("PyBank","budget_data.csv")
budget_data = pd.read_csv(filepath)

# get the total months included in the dataset
total_mon = len(budget_data)

# the net total amount over the entire period
net_profit = sum(budget_data["Profit/Losses"])


# the average of the changes over the entire period
avg_changes = net_profit/total_mon

# initiate a list for step increases
inc = []

# the greatest increase in profits (date and amount) over the entire period
for i in range(total_mon-1):
    difference = budget_data["Profit/Losses"][i + 1] - budget_data["Profit/Losses"][i]
    inc.append(difference)

# find maximun increase and decrease in profits
maximun_increase = max(inc)
maximun_decrease = min(inc)
# find corresponding month for maximun increase and decrease in profits
max_month = budget_data["Date"][inc.index(maximun_increase)+1]
min_month = budget_data["Date"][inc.index(maximun_decrease)+1]

# variable assignment (results with strings for print-out)
fncl_anls = f'Financial Analysis\n----------------------'
tol_mon = f'Total Months: {total_mon}'
total = f'Total: ${net_profit}'
avg_chan = f'Average Changes: $'
profits_in_de = f'Greatest Increase in Porfits: {max_month} (${maximun_increase})\nGreatest Decrease in Profits: {min_month} (${maximun_decrease})'

#print results as described
print(fncl_anls)
print(tol_mon)
print(total)
print(avg_chan)
print(profits_in_de)

# store results in a list
results_pybank = [fncl_anls,tol_mon,total,avg_chan,profits_in_de]

# write financial analysis results into a new text file
with open("PyBank\\PyBank_Results.txt", "w", newline = "") as results:
    for i in results_pybank:
        results.write(i)
        results.write('\n')
# or use results.writelines to write the list results_pybank

#close text file
results.close()
