import pyfiglet

text = pyfiglet.figlet_format('love you baby and vaishu more than you',font = 'puffy')

print(text)

print('to get the list of fonts',pyfiglet.FigletFont.getFonts())

"""Python has a cool library that you can use to generate custom 
fonts. This library is designed for the purpose of creating fancy 
texts for our programs. For example, we can use a generated 
font to create a cool article title. Below, we are going to 
demonstrate how we can create a fancy title with the module. 
Install with pip;
pip install pyfiglet
The figlet_format() method takes two arguments: the text we 
want to format and the font. The font parameter is optional. If 
we do not pass an argument for the font, the default font will be 
applied to our text"""