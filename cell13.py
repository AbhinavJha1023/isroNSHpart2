plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
sns.barplot(x='Type_of_Renewable_Energy', y='Initial_Investment_USD', data=grouped_df, palette='viridis')
plt.title('Initial Investment by Type')
plt.xlabel('Type of Renewable Energy')
plt.ylabel('Initial Investment (USD)')
plt.xticks(ticks=range(7), labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])

plt.subplot(1, 2, 2)
sns.barplot(x='Type_of_Renewable_Energy', y='Financial_Incentives_USD', data=grouped_df, palette='viridis')
plt.title('Financial Incentives by Type')
plt.xlabel('Type of Renewable Energy')
plt.ylabel('Financial Incentives (USD)')
plt.xticks(ticks=range(7), labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])

plt.tight_layout()
plt.show()
