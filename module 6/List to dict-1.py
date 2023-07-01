my_list = ['@F1', 'ABOD', '@F2', 'GHO', '@F3', 'RTYF', '@F4', 'SAVR']

my_dict = {}

for indx, val in enumerate(my_list):
    if val[0] == '@':
        my_dict[val] = my_list[indx+1]

print(my_dict)