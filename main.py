"""
main.py
Description: Python script to monitor and visualize CPU and memory usage in real-time 
    using Matplotlib for plotting and Psutil for system information.
Author: Giulia Valvano
Data: 29/05/2026
Version: 1.0
"""

# libraries 
import matplotlib.pyplot as plt # used for plotting
import matplotlib.animation as animation # used for animation
from plot import fig
from update import update

# animation
ani = animation.FuncAnimation(fig, update, interval=100, blit=True, cache_frame_data=False)

# show plot with animation
plt.show()