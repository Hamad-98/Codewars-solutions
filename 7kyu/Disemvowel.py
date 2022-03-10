def disemvowel(string):
    newWord = ''

    for word in string:
        if word not in 'aeiouAEIOU':
            newWord += word
    
    return newWord
  
"""
one-liner
"""

def disemvowel(string):
    return ''.join(word for word in string if word not in 'aeiou')
  
  
"""
Below solution cleans up any trailing/leading whitespace
Ex: 'This is a test' -> 'Ths s tst'
"""

def disemvowel(string):
  n = ''

  for word in string:
    if word not in 'aeiouAEIOU':
      n+= word

  return ' '.join(n.split())  
  
