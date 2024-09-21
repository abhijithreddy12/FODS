import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = [30, 32, 35, 40, 45, 50, 55, 53, 48, 42, 35, 32]  # Monthly temperature data
rainfall = [100, 120, 80, 60, 30, 20, 10, 15, 50, 90, 110, 130]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.plot(months, temperature, marker='o', linestyle='-', color='r')
ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (°C)')
ax1.set_title('Monthly Temperature Data (Line Plot)')
ax1.set_xticklabels(months, rotation=45)
ax1.grid(True)

ax2.scatter(months, rainfall, color='b')
ax2.set_xlabel('Month')
ax2.set_ylabel('Rainfall (mm)')
ax2.set_title('Monthly Rainfall Data (Scatter Plot)')
ax2.set_xticklabels(months, rotation=45)
ax2.grid(True)

plt.tight_layout()

# Show both plots
plt.show()
