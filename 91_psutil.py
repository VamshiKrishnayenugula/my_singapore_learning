"""want to know the resources your machine is using? 
Python has a library called psutil that calculates the resource 
usage of a computer. You can find out how much RAM and 
CPU your computer is using with just a few lines of code. 
Install the library using pip:
pip install psuti"""

import psutil

memory = psutil.virtual_memory()

def ram_usage():
    print(f'total memory is {memory.total/(2024**3):.2f}')
    print(f'Total used memory in gigabytes  {memory.used/(1024**3):.3f}')
    print(f'Percentage of memory under use:{memory.percent}%')




ram_usage()


"""If we want to know the CPU usage of the machine, we can use 
psutil.cpu_percent. This will return a usage percentage for 
each CPU on the machine. If I run this on the machine I am 
using now, here is what I get"""




import psutil
cpu_core = psutil.cpu_percent(percpu=True)
for cpu, usage in enumerate(cpu_core):
 print(f"# {cpu+1} CPU: {usage}%")
