# Write a program to print out the capital letters in the string
# "Alright, but apart from the Sanitation, the Medicine, Education,
# Wine, Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?"
# Check out the string methods for one way to test if a character is in uppercase.

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

strinOfCapitalLetters = ""

for q in quote :
    if q.isupper() :
       # print(q)
        strinOfCapitalLetters = strinOfCapitalLetters+q
    else: continue
print(strinOfCapitalLetters)

# print(quote.isupper())
#
# words = quote.split()
# print(words)
# for w in words :
#     print(any(w.isupper()))