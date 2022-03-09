def get_count(sentence):
    counter = 0
    for word in sentence:
        if word in 'aeiouAEIOU':
            counter+=1
    return counter
