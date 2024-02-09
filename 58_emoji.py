import demoji

text = " i am ☺️🙂😊😀😁 ☹️🙁😞😟😣😖😨😧😦😱😫😩😗😙😚😘😍"

print(demoji.findall(text) , end=" ")



# to get the output in line by line


# Find all emojis in the text
emojis = demoji.findall(text)

# Print each emoji on a new line
for emoji in emojis.values():
    print(emoji)


for i,j in emojis.items():
    print(i,j)