import os
from glob import glob

os.system('python3 models/download_models.py')
os.system('wget https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg -O examples/inputs/its.jpg')
os.system('wget https://upload.wikimedia.org/wikipedia/commons/f/ff/Camille_Pissarro_-_Boulevard_Montmartre%2C_Spring_-_Google_Art_Project.jpg -O montmartre.jpg')
os.system('wget https://upload.wikimedia.org/wikipedia/commons/5/56/Isaak_Ilitsch_Lewitan_005.jpg -O levitan.jpg')

nama_lokasi = ['surabaya_levitan','surabaya_montmartre','its_montmartre','surabaya_waveoff' ]

for lokasi in nama_lokasi:
    try:
        os.mkdir(f'{lokasi}/')
    except:
        pass

for script in glob('*.sh'):
    os.system(f'bash {script}')