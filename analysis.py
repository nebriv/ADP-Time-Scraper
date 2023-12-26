import pandas as pd
import matplotlib.pyplot as plt
import json

# Function to convert hours:minutes to days based on a 7-hour workday
def convert_to_days(time_str):
    hours, minutes = map(int, time_str.split(':'))
    total_minutes = hours * 60 + minutes
    return total_minutes / (7 * 60)  # Convert minutes to 7-hour workdays

# Load data from JSON file
with open('output_good.json', 'r') as file:
    data = json.load(file)

# Parsing data
vacation_data = {list(d.keys())[0]: convert_to_days(list(d.values())[0]) for d in data['vacation']}
sick_data = {list(d.keys())[0]: convert_to_days(list(d.values())[0]) for d in data['sick']}

# Creating DataFrame
df = pd.DataFrame({'Vacation': vacation_data, 'Sick': sick_data})

# Converting index to datetime
df.index = pd.to_datetime(df.index)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Vacation'], label='Vacation', marker='o')
plt.plot(df.index, df['Sick'], label='Sick', marker='x')

plt.title('Accrued Vacation and Sick Time')
plt.xlabel('Week')
plt.ylabel('Time in Days')

# Set x-axis labels with fewer labels
label_interval = 8  # Adjust this number based on your preference
x_ticks = df.index[::label_interval]
plt.xticks(x_ticks, [label.strftime('%Y-%m-%d') for label in x_ticks], rotation=45, ha='right')

plt.legend()
plt.tight_layout()

# Show plot
plt.show()
