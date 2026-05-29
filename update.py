"""
update.py
Description: script to update the plot for real-time CPU and memory usage monitoring.
Author: Giulia Valvano
Data: 29/05/2026
Version: 1.0
"""

# libraries 
from collections import deque # used to store history with a maximum size
from cpu_memory import get_cpu_memory
from plot import ax, cpu_line, memory_line, cpu_text, memory_text

# maximum history size
MAX_POINTS = 250

# lists to store history
x_data = deque(maxlen=MAX_POINTS)
cpu_data = deque(maxlen=MAX_POINTS)
memory_data = deque(maxlen=MAX_POINTS)

def update(frame):

    # get values of CPU and memory usage
    cpu_usage, memory_usage = get_cpu_memory()

    # save history
    x_data.append(frame)
    cpu_data.append(cpu_usage)
    memory_data.append(memory_usage)

    # update lines
    cpu_line.set_data(x_data, cpu_data)
    memory_line.set_data(x_data, memory_data)

    # moving window
    ax.set_xlim(max(0, frame - MAX_POINTS), frame + 1)

    # update text
    cpu_text.set_text(f'CPU: {cpu_usage:.1f}%')
    memory_text.set_text(f'Memory: {memory_usage:.1f}%')

    return cpu_line, memory_line, cpu_text, memory_text