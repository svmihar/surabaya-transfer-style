import os
from glob import glob

os.system('python3 models/download.py')

nama_lokasi = ['surabaya_montmartre','its_montmartre','surabaya_waveoff' ]

for lokasi in nama_lokasi:
    try:
        os.mkdir(f'{lokasi}/')
    except:
        pass

for script in glob('*.sh'):
    os.system(f'bash {script}')