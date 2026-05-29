"""
cpu_memory.py
Description: script to get CPU and memory usage values.
Author: Giulia Valvano
Data: 29/05/2026
Version: 1.0
"""

# libraries 
import psutil # used to get CPU and memory usage

def get_cpu_memory():

    # get values of CPU and memory usage
    cpu_usage = psutil.cpu_percent(interval=None)
    memory_usage = psutil.virtual_memory().percent

    return cpu_usage, memory_usage