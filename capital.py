s = 'alert. boss! oh'
signs = (".", "!", "?")
strip_words = []
words = s.split(" ")
words[0] = words[0].title()
for word in words:
    strip_words.append(word.strip())
words=[]
for i, word in enumerate(strip_words):
    print(i, word)
    if word.endswith(signs) and len(strip_words)-i>1:
        strip_words[i+1] = strip_words[i+1].title()
    words.append(word)
    print(words)
text = " ".join(words)
print(text)
