def number_words(text):
   words= text.split()
   num= len(words)
   return num

def count_characters(text):
    c_characters={}
    words= text.split()
    count=0
    for word in words:
        lowercase= word.lower()
        for letter in lowercase:
            if letter not in c_characters:
               c_characters[letter]=1
            else:
               c_characters[letter]+=1
    return c_characters

def sort_on(c_characters):
   r_characters=[]
   letter= list(c_characters)
   for character in letter:
       r_charact={}
       r_charact["char"]= character
       r_charact["num"]= c_characters[character]
       r_characters.append(r_charact)
   r_characters.sort(reverse=True, key= sorter)
   return r_characters

def sorter(items):
    return items["num"]

