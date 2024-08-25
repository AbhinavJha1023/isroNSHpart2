# Group by type of renewable energy and calculate mean values
grouped_df = df.groupby('Type_of_Renewable_Energy').mean().reset_index()

# Plot installed capacity, energy production, and energy consumption
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.barplot(x='Type_of_Renewable_Energy', y='Installed_Capacity_MW', data=grouped_df, palette='viridis')
plt.title('Installed Capacity by Type')
plt.xlabel('Type of Renewable Energy')
plt.ylabel('Installed Capacity (MW)')
plt.xticks(ticks=range(7), labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])

plt.subplot(1, 3, 2)
sns.barplot(x='Type_of_Renewable_Energy', y='Energy_Production_MWh', data=grouped_df, palette='viridis')
plt.title('Energy Production by Type')
plt.xlabel('Type of Renewable Energy')
plt.ylabel('Energy Production (MWh)')
plt.xticks(ticks=range(7), labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])

plt.subplot(1, 3, 3)
sns.barplot(x='Type_of_Renewable_Energy', y='Energy_Consumption_MWh', data=grouped_df, palette='viridis')
plt.title('Energy Consumption by Type')
plt.xlabel('Type of Renewable Energy')
plt.ylabel('Energy Consumption (MWh)')
plt.xticks(ticks=range(7), labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])

plt.tight_layout()
plt.show()
