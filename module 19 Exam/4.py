
anagrams = ['eat', 'ate', 'done', 'tea', 'soup', 'node']

grouped_anagrams = {}

for string in anagrams:
   # print(string)
   sorted_string = str(sorted(string))
   # print(sorted_string)

   if sorted_string in grouped_anagrams:
      grouped_anagrams[sorted_string].append(string)
   else:
      grouped_anagrams[sorted_string] = [string]

print(list(grouped_anagrams.values()))

