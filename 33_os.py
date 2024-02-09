"""import os
print(os.path.exists('one.txt'))
with open('one.txt') as f:
    f.read()
"""

import os

file_path = 'D:\My_learning\Data_Camp\Functions\hundred\one.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        print(content)
else:
    print(f"The file '{file_path}' does not exist.")
