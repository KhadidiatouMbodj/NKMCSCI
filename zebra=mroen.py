
#this program prints caesar cipher.

#Predict what will be printed:
    
	    
message = input('')
newMessage = ""
for c in message:
    offset = ord(c) - ord('a') + 13 
    wrap = offset % 26
    newChar = chr(ord('a') + wrap)
    print(wrap,chr(ord('a')+13))    
    newMessage = newMessage + newChar
print("The coded message is", newMessage)
	

word = "zebra"
codedWord = ""
for ch in word:
    offset = ord(ch) - ord('a') + 13 
    wrap = offset % 26  
    newChar = chr(ord('a') + wrap)  
    print(wrap, chr(ord('a') + wrap))    
    codedWord = codedWord + newChar 
	    
print("The coded word (with wrap) is", codedWord)
