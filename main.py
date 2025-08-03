import sys

def get_book_text (filepath):
   with open(filepath) as f:
       file_contents= f.read()
   return file_contents

from stats import number_words
from stats import count_characters
from stats import sort_on

def main():
   book_path= sys.argv[1] 
   book_text= get_book_text(book_path)
   num_words= number_words(book_text)
   num_total= f"{num_words} words found in the document"
   count_c= count_characters(book_text)
   sort= sort_on(count_c)
   print ("============ BOOKBOT ============")
   print (f"Analyzing book fount at {book_path}")
   print ("---------- Word Count ----------")
   print (f"Found {num_words} total words")
   print ("--------- Character Count -------")
   for dictionary in sort:
       if dictionary["char"].isalpha():
          print (f'{dictionary["char"]}: {dictionary["num"]}')
   print ("============= END ===============")

if len(sys.argv) < 2:
   print ("Usage: python3 main.py <path_to_book>")
   sys.exit(1)
else:
   main()


