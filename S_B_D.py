import matplotlib.pyplot as plt
import pandas as pd

# Data for primary growth (total weight lifted)
data = {
    'Week': [1, 2, 3, 4, 5, 6],
    "Total_Weight": [50, 100, 150, 200, 250, 300],
    "Estimated_1RM": [60, 120, 180, 240, 300, 360]  # Example secondary growth data (Estimated 1RM)
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Plotting Primary and Secondary Growth
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
    'Squad':[50,100,150,200,250,300]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))

plt.plot(df['Week'], df['Squad'], label='squad', color='Red', marker='o')

plt.title('Growth of 5 weeks')
plt.xlabel('Week')
plt.ylabel('Load(S)')
plt.legend()
plt.grid(True)




data = {
    'Week': [1, 2, 3, 4, 5, 6],
    'Bench':[50,100,150,200,250,300]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))

plt.plot(df['Week'], df['Bench'], label='Bench', color='Blue', marker='o')
plt.title('Growth of 5 weeks')
plt.xlabel('Week')
plt.ylabel('Load(S)')
plt.legend()
plt.grid(True)




data = {
    'Week': [1, 2, 3, 4, 5, 6],
    'Deadlift':[50,100,150,200,250,300]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))

plt.plot(df['Week'], df['Deadlift'], label='Deadlift', color='Green', marker='o')
plt.title('Growth of 5 weeks')
plt.xlabel('Week')
plt.ylabel('Load(S)')
plt.legend()
plt.grid(True)

plt.show()