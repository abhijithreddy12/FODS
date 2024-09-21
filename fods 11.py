import matplotlib.pyplot as plt

days = list(range(1, 31))  
sales = [100, 150, 130, 170, 180, 190, 140, 160, 200, 210, 220, 230, 250, 240, 260, 270, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420]  # Sales data for each day

plt.figure(figsize=(10, 6))
plt.plot(days, sales, marker='o', linestyle='-', color='b')


plt.xlabel('Day of the Month')
plt.ylabel('Sales ($)')
plt.title('Daily Sales in a Month (Line Plot)')
plt.grid(True)

plt.tight_layout()
plt.show()
plt.scatter(days, sales, color='r')

plt.xlabel('Day of the Month')
plt.ylabel('Sales ($)')
plt.title('Daily Sales in a Month (Scatter Plot)')
plt.grid(True)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

days = list(range(1, 31))  
sales = [100, 150, 130, 170, 180, 190, 140, 160, 200, 210, 220, 230, 250, 240, 260, 270, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420]  # Sales data for each day

plt.figure(figsize=(10, 6))
plt.bar(days, sales, color='g')

plt.xlabel('Day of the Month')
plt.ylabel('Sales ($)')
plt.title('Daily Sales in a Month (Bar Plot)')
plt.xticks(days, rotation=45) 
plt.tight_layout()
plt.show()
