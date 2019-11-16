import os

files = os.listdir()

for file in files: 
    if file.split('_')[0].isdigit(): 
        print(file)
        os.system(f'rm {file}')
