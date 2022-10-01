# Importing modules
import csv
import os

# Specify the file to open and create to
file_to_load = os.path.join("..", '**PyBank**', 'budget_data.csv')

# Specify the file to export text file to
file_to_output = os.path.join("..", '**PyBank**', 'budget_analysis.txt')


# Track various financial parameters
months_total = 0
month_of_change = []
net_change_list = []
gi = ["", 0]
gd = ["", 9999999999999999999]
total_net = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    months_total += 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total
        months_total += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        # Calculate the greatest increase
        if net_change > gi[1]:
            gi[0] = row[0]
            gi[1] = net_change

        # Calculate the greatest decrease
        if net_change < gd[1]:
            gd[0] = row[0]
            gd[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months_total}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {gi[0]} (${gi[1]})\n"
    f"Greatest Decrease in Profits: {gd[0]} (${gd[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

