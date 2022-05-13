#manual with right distance for each word

FrameContentList = ["Circle", "in", "a", "frame"]
TopBottomFrame = ('**********')

print(TopBottomFrame)
print('* ' + FrameContentList[0] + ' *')
print('* ' + FrameContentList[1] + ' ' + ' ' + ' ' + ' '+ ' *')
print('* ' + FrameContentList[2] + ' ' + ' ' + ' ' + ' '+ ' '+ ' *')
print('* ' + FrameContentList[3] + ' '+ ' *')

print(TopBottomFrame)

#automated1
FrameContentList = ["Circle", "in", "a", "frame", "without", "distance"]
TopBottomFrame = ('**********')

print(TopBottomFrame)

for word in FrameContentList:
    print('* ' + word + ' *')

print(TopBottomFrame)


#automated 2
# the function should 
# 1. take the first item out of the list
# 2. count the word length
# 3. substract it from 6 (e.g. 10 stars - (first star + space) - (space + last star))
# 4. remainder is number of spaces after word
# 5. set variable space = ' '
# 


FrameContentList = ["Circle", "in", "a", "frame", "with", "the", "right", "distance"] #max 6-letter words!
TopBottomFrame = ('************')
spaceAfterWord = (' ')

print(TopBottomFrame)

for word in FrameContentList:
    print('* ' + word + (8-len(word))*spaceAfterWord + ' *')

print(TopBottomFrame)

# Frame with complete automation: op line orients itself on longest word in the list and ads 4
FrameContentList = ["Circle", "in", "a", "frame", "with", "supervariable", "distance"] #no limit
singleStar = ('*')
spaceAfterWord = (' ')
countLetters = len(max(FrameContentList, key=len)) # finds longest word/string based on length with max() and key, len() converts into int

TopBottomFrame = ((countLetters + 4) * singleStar) # determines length of top and bottom line by taking number of longest word, adding 4 digits (for beginning and end + 1 space each )
print(TopBottomFrame)

for word in FrameContentList:
    print('* ' + word + (countLetters - len(word)) * spaceAfterWord + ' *')
# takes each item/ word of the list and puts it between the stars together with the corresponding spaces to make the vertical end line even

TopBottomFrame = ((countLetters + 4) *singleStar)
print(TopBottomFrame)

