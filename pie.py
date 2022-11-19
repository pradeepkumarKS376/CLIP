# MatPlotLib
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np

# Pie Chart
def piechart(request):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Sale', 'Purchase'
    sizes = [random.randint(10,30), random.randint(30,50)]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('media/sale_purchase_peichart.png',dpi=100)
    return render(request,'Home.html')