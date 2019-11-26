import os
from glob import glob
from pprint import pprint
import time

os.system('python3 models/download_models.py')
#os.system('wget https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg -O examples/inputs/its.jpg')
os.system('wget https://upload.wikimedia.org/wikipedia/commons/f/ff/Camille_Pissarro_-_Boulevard_Montmartre%2C_Spring_-_Google_Art_Project.jpg -O montmartre.jpg')
#os.system('wget https://upload.wikimedia.org/wikipedia/commons/5/56/Isaak_Ilitsch_Lewitan_005.jpg -O levitan.jpg')
#os.system('wget https://upload.wikimedia.org/wikipedia/commons/6/66/Claude_Monet_-_The_Water_Lilies_-_Setting_Sun_-_Google_Art_Project.jpg -O lily.jpg')
#os.system('wget https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Isaac_Levitan_-_Golden_autumn._Slobodka_-_Google_Art_Project.jpg/1600px-Isaac_Levitan_-_Golden_autumn._Slobodka_-_Google_Art_Project.jpg -O examples/inputs/autumn.jpg')
if os.path.exists('starry.jpg'): 
    pass
else: 
    os.system('wget https://upload.wikimedia.org/wikipedia/commons/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg -O starry.jpg')

nama_lokasi = ['surabaya_levitan','surabaya_montmartre', 'p_on_p', 'starry_night']

for lokasi in nama_lokasi:
    try:
        os.mkdir(f'{lokasi}/')
    except:
        pass

pilihan = {0:'all'}
for i,script in enumerate(glob('run_script/*.sh')):
    print(f" {i+1}:{script}")
    pilihan[i+1]=script
pprint(pilihan)
user_input = int(input('pilih salah satu:\n> '))
assert user_input in pilihan.keys(), 'input is not recognized'
start = time.time()
if user_input == 0 : 
    for k,v in pilihan.items(): 
        os.system(f'bash {v}')
else:
    os.system(f'bash {pilihan[user_input]}')
print(time.time()- start)
