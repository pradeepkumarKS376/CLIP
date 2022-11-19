import matplotlib.pyplot as plt

sizes= [50,40, 10]
mylabels = ["InProgress", "Success", "Over Due"]
myexplode = [0, 0, 0]
mycolors = ["blue", "green", "red"]
#Data = plt.pie(sizes, labels=mylabels, explode=myexplode, colors=mycolors)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=myexplode, labels=mylabels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()

