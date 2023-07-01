'''
Object processor
'''
from zipfile import ZipFile
import glob
import shutil
import os

sourch_path = '../source/*'
destination_path = '../destination'




sourch_obj = glob.glob(sourch_path)
# print(sourch_obj)

obj_path = sourch_obj[0]
# print(obj_path)

extension = obj_path.split("\\")
# print(extension[1])

text_file = extension[0]+'/'+extension[1]

for i in range(1, 4):
    with open(text_file, 'r') as file:
        lines = file.read().split('\n')
        desired_lines = lines[0:i*10:]
        file = open(f'../server/some{i}.txt', 'w')
        for line in desired_lines:
            file.write(line)
            file.write('\n')
    file.close()

sourch_path2 = '../server/*'

obj_path2 = glob.glob(sourch_path2)
# print(obj_path2)

for i in range(1, len(obj_path2)):
    new_obj = obj_path2[i].split('\\')[1]
    # print(new_obj)
    zip_file = shutil.make_archive('sabbirzip', 'zip', new_obj)
    # shutil.copy(new_obj, f'{destination_path}/{new_obj}')
    with ZipFile(zip_file.zip, 'r') as zObject:
        # shutil.copy(zip_file, destination_path)
        zObject.extractall(path=destination_path)
  
    
   


# while True:
#     sourch_obj = glob.glob(sourch_path)
#     # print(sourch_obj)
#     if len(sourch_obj) > 0:

#         obj_path = sourch_obj[0]
#         shutil.copy(obj_path, '.')

#         obj_name = obj_path.split('\\')[-1].split('.')
#         prifix = obj_name[0]
#         prifix2 = obj_name[1]

#         for item in range(len(postfix)):
#             file_name = prifix  + '_' + str(item) + '.'+ prifix2
#             print(file_name)
#             shutil.copy(obj_path, f'{destination_path}/{file_name}')

#         os.remove(obj_path)
#         os.remove(obj_path.split('\\')[-1])