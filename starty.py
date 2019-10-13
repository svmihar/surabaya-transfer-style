import os
from glob import glob

nama_lokasi = ['surabaya_luncheon','surabaya_montmartre','its_montmartre','surabaya_waveoff' ]
for lokasi in nama_lokasi:
    os.mkdir(f'{lokasi}/')

for script in glob('*.sh'):
    os.system(f'bash {script}')