plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
sns.barplot(x='Type_of_Renewable_Energy', y='GHG_Emission_Reduction_tCO2e', data=grouped_df, palette='viridis')
plt.title('GHG Emission Reduction by Type')
plt.xlabel('Type of Renewable Energy')
plt.ylabel('GHG Emission Reduction (tCO2e)')
plt.xticks(ticks=range(7), labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])

plt.subplot(1, 2, 2)
sns.barplot(x='Type_of_Renewable_Energy', y='Jobs_Created', data=grouped_df, palette='viridis')
plt.title('Jobs Created by Type')
plt.xlabel('Type of Renewable Energy')
plt.ylabel('Number of Jobs Created')
plt.xticks(ticks=range(7), labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])

plt.tight_layout()
plt.show()
