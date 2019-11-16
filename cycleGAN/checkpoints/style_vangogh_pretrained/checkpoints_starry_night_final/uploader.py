import os, time



for i in range(3):
    print(i+1)
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
    os.system('drive add_remote')
    print(f'now sleeping for 3 hours from {time_string}')
    time.sleep(10800)
    print('finished uploading')
