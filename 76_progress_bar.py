"""When you are executing loops (especially really large ones), you 
can show a smart progress bar. A library called tqdm creates a 
progress meter that keeps track of the progress of your loop. To 
install the library, run:
Pip install tqdm 
Let’s say you have a range of 100000 that you want your loop to 
run through, and after every loop, you want your code to sleep 
for 0.001 sec. Here's how to do it with tqdm so you can monitor 
the loop's progress. When you run this code, you will get the 
progress meter below as the output."""

from tqdm import tqdm
from time import sleep

for i in tqdm(range(1000)):
    sleep(0.001)
