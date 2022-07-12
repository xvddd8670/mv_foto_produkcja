import os
import shutil
import logging
import traceback

from progress.bar import ShadyBar

#create config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='log')
logging.info('               ')
logging.info('+++++++++++++++')
logging.info('start programm')

files_list = []
info_files_list = []

path_for_foto = 'volume1/FTP/'
path_for_mv_foto = 'volume2/kamery_produkcja/'

for item in os.listdir(path_for_foto):
    if item[-4:] == '.jpg':
        files_list.append(item)

#create info list
logging.info('create file list')
print('create file list')
bar = ShadyBar('', max=len(files_list))
errors = False
i_in_while = 0
while i_in_while < len(files_list):
    info = ['', '']
    d_n = 0
    j_in_while = len(files_list[i_in_while])-5
    ##
    while True:
        try:
            if files_list[i_in_while][j_in_while] == '_':
                if d_n == 0:
                    j_in_while -= 7
                d_n += 1
                if d_n == 2:
                    break
            else:
                info[d_n] += files_list[i_in_while][j_in_while]
            j_in_while -= 1
        except:
            logging.warning('wrong format filename. skip.')
            del files_list[i_in_while]
            errors = True
            break
    ##
    if errors == True:
        errors = False
        continue
    ##
    info[0] = info[0][::-1]
    info[1] = info[1][::-1]
    info[1] = info[1].replace('-', '_')
    info[1] = info[1][0:7]
    info_files_list.append(info)
    i_in_while += 1
    bar.next()
bar.finish()

workplaces_set = []
dates_set = []
for item in info_files_list:
    workplaces_set.append(item[0])
    dates_set.append(item[1][0:7])

workplaces_set = set(workplaces_set)
dates_set = set(dates_set)

workplaces_set = list(workplaces_set)
dates_set = list(dates_set)

#create folders
logging.info('create folders')
print('create folders')
bar = ShadyBar('', max=len(dates_set))
i_in_while = 0
while i_in_while < len(dates_set):
    if not os.path.exists(path_for_mv_foto+dates_set[i_in_while]):
        os.mkdir(path_for_mv_foto+dates_set[i_in_while])
    i_in_while += 1
    bar.next()
bar.finish()

#move files
logging.info('move files')
print('move files')
bar = ShadyBar('', max=len(files_list))
i_in_while = 0
while i_in_while < len(files_list):
    ##
    try:
        shutil.move(path_for_foto+files_list[i_in_while], path_for_mv_foto+info_files_list[i_in_while][1])
        os.system('chmod 777 /'+path_for_mv_foto+info_files_list[i_in_while][1]+'/'+files_list[i_in_while])
        #print(info_files_list[0])
        #print(info_files_list[1])
    except:
        logging.warning('duplicate. save both files.')
        err = traceback.format_exc()
        err = err[-15:-1]
        if err == 'already exists':
            new_name = '0'+files_list[i_in_while]
            os.rename(path_for_foto+files_list[i_in_while], path_for_foto+new_name)
            files_list[i_in_while] = new_name
            continue
        else:
            logging.error('====================')
            logging.error(traceback.format_exc())
            logging.error('====================')
    i_in_while += 1
    bar.next()
bar.finish()

logging.info('end programm')
logging.info('+++++++++++++++')
logging.info('               ')





























'''
try:
    files_list
    print('ok')
except:
    print('create')
'''


'''
for file in files_list:
    print(file)
'''
















