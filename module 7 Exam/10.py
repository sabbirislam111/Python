a = ['Oh,', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

for word in s.split():
    if word in a:
      print(word)
