# Secret Message Decoder
#Take a message and a word. Check, ignoring case, whether the word is in the message. Print how many times itappears and where it first appears.

message = input("Enter your message:")
word= input("Enter the word to search for: ")

message_lower = message.lower()
word_lower = word.lower()

count = message_lower.count(word_lower) 
position = message_lower.find(word_lower)

if count>0:
    print("The word appears in the message",count,"times.")
    print("The first occurrence of the word is at index",position)
else:
    print("The word does not appear in the message.")