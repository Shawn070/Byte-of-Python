import os
import time

source = ['/data/data/com.termux/files/home/python_machine']
target_dir = '/data/data/com.termux/files/home/Backup/'
target = target_dir + os.sep + \
        time.strftime('%Y%m%d%H%M') + '.zip'

if not os.path.exists(target_dir):
    print('There is not such backup file, we\'ll built it.')
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target, \
        ' '.join(source))

print('Zip commad is:')
print(zip_command)
print('Running:')

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILD')
