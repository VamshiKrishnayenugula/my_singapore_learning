"""An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
 using all the original letters exactly once. In other words, the two words or phrases are 
anagrams if they have the same characters but may be in a different order."""

from collections import Counter
a = 'vamshi'
b = 'ishvam'
c = 'ishvaM'
print('check anagram or not  :  ',Counter(a)==Counter(b))

print('check anagram or not  :  ',Counter(a)==Counter(c))
