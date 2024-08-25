plt.figure(figsize=(10, 6))
sns.scatterplot(x='Energy_Production_MWh', y='Energy_Consumption_MWh', hue='Type_of_Renewable_Energy', palette='viridis', data=df)
plt.title('Energy Production vs. Consumption')
plt.xlabel('Energy Production (MWh)')
plt.ylabel('Energy Consumption (MWh)')
plt.legend(title='Type of Renewable Energy', labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])
plt.show()
