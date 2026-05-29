# CPU and Memory Monitor
This project builds a simple real-time CPU and memory monitoring system using Python, Matplotlib, and Psutil.
The application displays dynamic graphs showing CPU and RAM usage over time.

---

## Features
- Real-time CPU monitoring
- Real-time memory monitoring
- Dynamic live graph updates
- Historical usage visualization
- Automatic scrolling graph
- Lightweight and simple interface
- Modular project structure
- Efficient memory handling using deque

---

## Technologies Used
- Python 3.14.5
- Matplotlib
- Psutil
- Collections (deque)

---

## Project Structure
```text
CPUMemoryMonitor/
│
├── main.py
├── update.py
├── cpu_memory.py
├── plot.py
│
└── README.md
```

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/giuliavalvano/CPUMemoryMonitor.git
```

---

### 2. Enter the project folder
```bash
cd CPUMemoryMonitor
```

---

### 3. Install dependencies
```bash
pip install matplotlib
pip install psutil
```

---

## Running the Project
```bash
python main.py
```

---
## How It Works

The application:
1. Collects CPU and memory usage data using Psutil
2. Stores historical data using deque
3. Updates the graph continuously using Matplotlib animation
4. Displays CPU and memory usage in real time
5. Automatically scrolls the graph window as new data arrives

---

## Real-Time Animation
The project uses Matplotlib FuncAnimation to create smooth real-time updates without reopening the graph window.

---

## Data History
The application stores a fixed amount of historical data using deque with maxlen to prevent excessive memory usage and maintain performance stability.
