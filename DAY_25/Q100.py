# Sort words by length 
def sort_by_length(sentence):
    words=sentence.split()
    n=len(words)
    for i in range(n-1):
        for j in range(n-i-1):
            if len(words[j])>len(words[j+1]):
                words[j],words[j+1]=words[j+1],words[j]
    return words
sentence="I love Python programming"
print(sort_by_length(sentence))
