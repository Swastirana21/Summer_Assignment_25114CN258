# Count words in a sentence 
def count_words(sentence):
    count=1
    for char in sentence:
        if char==" ":
            count+=1
    return count
sentence="Hello World this is Python"
print(count_words(sentence))


