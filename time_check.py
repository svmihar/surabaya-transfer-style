import time
import subprocess as sp

start = time.time()
sp.call(['bash', 'starry_bigger_time.sh'])
print(f'running duration: {time.time() - start}')