# Group by type of renewable energy and calculate summary statistics for storage efficiency
efficiency_summary = df.groupby('Type_of_Renewable_Energy')['Storage_Efficiency_Percentage'].describe()

print(efficiency_summary)

# Plot storage efficiency distributions
plt.figure(figsize=(10, 6))
sns.boxplot(x='Type_of_Renewable_Energy', y='Storage_Efficiency_Percentage', data=df, palette='viridis')
plt.title('Storage Efficiency by Type of Renewable Energy')
plt.xlabel('Type of Renewable Energy')
plt.ylabel('Storage Efficiency (%)')
plt.xticks(ticks=range(7), labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])
plt.show()
