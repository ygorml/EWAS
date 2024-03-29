import os
from datetime import datetime

# Arquivos que conterão os logs:
# log_comm_server.txt, log_control.txt, log_ew.py, log_nav.txt, log_safety.txt
# type 0: core_server,
# type 1: control,
# type 2: ew,
# type 3: nav,
# type 4: safety
# type 5: comm_server

def getFile(type):
    if type == 0:
        file = 'core_server.txt'
    elif type == 1:
        file = 'control.txt'
    elif type == 2:
        file = 'ew.txt'
    elif type == 3:
        file = 'nav.txt'
    elif type == 4:
        file = 'safety.txt'
    elif type == 5:
        file = 'comm_server.txt'
    return file

def logWrite(type, info):
    file = getFile(type)
    date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    with open(file, 'a') as fileHandler:
        fileHandler.write("{} - {}\n".format(date, info))

def resetLogs(type):
    file = getFile(type)
    os.remove(file)
    print("{} removido!\n".format(file))