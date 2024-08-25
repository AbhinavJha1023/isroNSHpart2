plt.figure(figsize=(10, 6))
sns.barplot(x='Type_of_Renewable_Energy', y='Jobs_Created', data=df, ci=None, palette='viridis')
plt.title('Number of Jobs Created by Different Types of Renewable Energy')
plt.xlabel('Type of Renewable Energy')
plt.ylabel('Number of Jobs Created')
plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6], labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])
plt.show()

