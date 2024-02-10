"""can add color to your code using pytohn and ansi escape codes"""

class Colors():
    Black = '\033[30m' 
    Green = '\033[32m' 
    Blue = '\033[34m' 
    Magenta = '\033[35m' 
    Red = '\033[31m' 
    Cyan = '\033[36m' 
    White = '\033[37m' 
    Yellow = '\033[33m' 

print(f'{Colors.Red} Warning: {Colors.White} I am vamshi')
