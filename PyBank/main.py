import os
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')

try:
    with open(budget_data_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
    
        csv_header = next(csv_reader)
        print("Financial Analysis")

        Total_Months = 0
        Net_Total_Profit_Loss = 0
        Prior_Profit_Loss = 0
        Change_in_Profit_Loss = 0
        Greatest_Increase_in_Profits = {"Date": "", "Profit/Losses": 0}
        Greatest_Decrease_in_Profits = {"Date": "", "Profit/Losses": 0}

        for row in csv_reader:
            Total_Months += 1
            Net_Total_Profit_Loss += int(row[1])

            if Total_Months > 1:
                change = int(row[1]) - Prior_Profit_Loss
                Change_in_Profit_Loss += change

                if change > Greatest_Increase_in_Profits["Profit/Losses"]:
                    Greatest_Increase_in_Profits["Profit/Losses"] = change
                    Greatest_Increase_in_Profits["Date"] = row[0]
                elif change < Greatest_Decrease_in_Profits["Profit/Losses"]:
                    Greatest_Decrease_in_Profits["Profit/Losses"] = change
                    Greatest_Decrease_in_Profits["Date"] = row[0]
                
            Prior_Profit_Loss = int(row[1])

        Average_Change = Change_in_Profit_Loss / (Total_Months - 1) if Total_Months > 1 else 0

        print("----------------------------")
        print(f"Total Months: {Total_Months}")
        print(f"Total: ${Net_Total_Profit_Loss}")
        print(f"Average Change: ${Average_Change:.2f}")
        print(f"Greatest Increase in Profits: {Greatest_Increase_in_Profits['Date']} (${Greatest_Increase_in_Profits['Profit/Losses']})")
        print(f"Greatest Decrease in Profits: {Greatest_Decrease_in_Profits['Date']} (${Greatest_Decrease_in_Profits['Profit/Losses']})")


        output_file_path = os.path.join("..", "analysis", "PyBank Analysis.txt")
        with open(output_file_path, 'w') as output_file:
            output_file.write("Financial Analysis\n")
            output_file.write("----------------------------\n")
            output_file.write(f"Total Months: {Total_Months}\n")
            output_file.write(f"Total: ${Net_Total_Profit_Loss}\n")
            output_file.write(f"Average Change: ${Average_Change:.2f}\n")
            output_file.write(f"Greatest Increase in Profits: {Greatest_Increase_in_Profits['Date']} (${Greatest_Increase_in_Profits['Profit/Losses']})\n")
            output_file.write(f"Greatest Decrease in Profits: {Greatest_Decrease_in_Profits['Date']} (${Greatest_Decrease_in_Profits['Profit/Losses']})\n")

        print(f"Results exported to: {output_file_path}")

except FileNotFoundError:
    print(f"Error: File '{budget_data_csv}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


