import webbrowser
url = "https://www.google.com/"
open_web = webbrowser.open(url)
print(open_web)

"""To open a website using Python, import the webbrowser 
module. This is a built-in module, so you don’t have to install 
anything. Below, we are trying to open google.com using the 
open() method of the module."""

"""You can also specify if you want to open a new tab in a browser 
or a new browser window. See the code below:"""
import webbrowser
url = "https://www.google.com/" 
 
# This opens a new tab in your browser 
webbrowser.open_new_tab(url)
# This opens a new browser window
webbrowser.open_new(url)