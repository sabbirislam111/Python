A = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."

set1=set()
# splitting the string  whenever we encounter a space
# string=A.split(" ")
# iterate through list-string
for i in A.split(' '):
    # Storing the word and its frequency in the form of tuple in a set
    # Set is used to avoid repetition
    set1.add((i,A.count(i)))
print(set1)