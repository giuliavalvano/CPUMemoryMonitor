"""
plot.py
Description: script to create the plot for real-time CPU and memory usage monitoring.
Author: Giulia Valvano
Data: 29/05/2026
Version: 1.0
"""

# libraries 
import matplotlib.pyplot as plt # used for plotting

# create figure
fig, ax = plt.subplots(figsize=(10, 5))

# title
fig.suptitle('CPU and Memory Usage Over Time')

# labels
ax.set_xlabel('Time (s)')
ax.set_ylabel('Usage (%)')

# initial limits
ax.set_ylim(0, 100)

# hide x ticks
ax.set_xticks([])

# enable grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# create lines
cpu_line, = ax.plot([], [], label='CPU Usage', color='blue')
memory_line, = ax.plot([], [], label='Memory Usage', color='red')

# text labels
cpu_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
memory_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)

# legend
ax.legend()

# adjust layout
plt.tight_layout()