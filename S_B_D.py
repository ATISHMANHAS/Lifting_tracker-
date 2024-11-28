import matplotlib.pyplot as plt
import pandas as pd

# Data for primary growth (total weight lifted)
data = {
    'Week': [1, 2, 3, 4, 5, 6],
    "Total_Weight": [ 100, 180, 220, 270, 300,320],
    "Estimated_1RM": [150, 200, 240, 290, 340, 360]  
}

# Convert data to DataFrame
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))

# Plot Primary Growth (Total Weight Lifted)
plt.plot(df['Week'], df['Total_Weight'], label='Primary Growth (Total Weight Lifted)', color='Red', marker='o')

# Plot Secondary Growth (Estimated 1RM)
plt.plot(df['Week'], df['Estimated_1RM'], label='Secondary Growth (Estimated 1RM)', color='Green', marker='o')

# Adding Titles and Labels
plt.title('Combined Primary and Secondary Growth Over Weeks')
plt.xlabel('Week')
plt.ylabel('Weight (kg)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()





# Data for primary growth (total weight lifted)
data = {
    'Week': [1, 2, 3, 4, 5, 6],
    'Squad':[50,80,140,180,200,220],
    'Secondary Growth':[100,150,180,220,250,290]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))

plt.plot(df['Week'], df['Squad'], label='squad', color='Red', marker='o')

plt.plot(df['Week'], df['Secondary Growth'], label='Secondary Growth (Secondary Growth)', color='Green', marker='o')

plt.title('Combined Primary and Secondary Growth Over Weeks ')
plt.xlabel('Week')
plt.ylabel('Load(S)')
plt.legend()
plt.grid(True)






data = {
    'Week': [1, 2, 3, 4, 5, 6],
    'Bench': [50, 70, 100, 140, 160, 190],
    'Secondary Growth': [80, 100, 140, 180, 200, 220],
    'Tempo': [40, 60, 100, 150, 200, 210]
}

df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))

# Plotting the data
plt.plot(df['Week'], df['Bench'], label='Bench', color='blue', marker='o')
plt.plot(df['Week'], df['Secondary Growth'], label='Secondary Growth', color='green', marker='o')
plt.plot(df['Week'], df['Tempo'], label='Tempo', color='red', marker='o')

# Adding title and labels
plt.title('Growth of 6 Weeks')
plt.xlabel('Week')
plt.ylabel('Load (S)')

# Adding legend and grid
plt.legend()
plt.grid(True)





data = {
    'Week': [1, 2, 3, 4, 5, 6],
    'Deadlift':[60,100,120,180,200,260],
    'Secondary Growth':[100,150,180,220,260,290]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))

plt.plot(df['Week'], df['Deadlift'], label='Deadlift', color='Green', marker='o')

plt.plot(df['Week'], df['Secondary Growth'], label='Secondary Growth (Secondary Growth)', color='Blue', marker='o')


plt.title('Growth of 5 weeks')
plt.xlabel('Week')
plt.ylabel('Load(S)')
plt.legend()
plt.grid(True)

plt.show()