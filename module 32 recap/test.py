dict = {"harun mollah": 80, "jomela": 70, "sabbir": 26, 'saleh': 27}

new_dict = {k: ("young" if v < 35 else "old") for k, v in dict.items()}
print(new_dict)