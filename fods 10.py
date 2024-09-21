import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [25000, 30000, 35000, 28000, 45000, 48000, 
         50000, 52000, 47000, 44000, 41000, 46000]

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)  
plt.plot(months, sales, marker='o', color='b', linestyle='-', label='Sales')
plt.title('Monthly Sales Data - Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.subplot(2, 1, 2) 
plt.bar(months, sales, color='g', label='Sales')
plt.title('Monthly Sales Data - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Show the plots
plt.show()



