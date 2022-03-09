def inside_out(st):
    n = st.split(' ')
    new=[]
    for word in n:
        if len(word)%2 == 0:
            firstHalf = word[0:(len(word)//2)][::-1]
            secondHalf = word[(len(word)//2):][::-1]
            word = firstHalf + secondHalf
            new.append(word)
        else:
            middle = len(word)//2
            middleLetter = word[len(word)//2]
            firstHalf = word[0:middle][::-1]
            secondHalf = word[middle+1:][::-1]
            word = firstHalf + middleLetter + secondHalf
            new.append(word)
            
    return ' '.join(new)
