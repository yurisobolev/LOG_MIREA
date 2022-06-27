import pathlib
import datetime
import threading
import pyAesCrypt
import io
import schedule

def MemoryCrypter(filename, is_encrypted):
    sequence_bytes = io.BytesIO()
    bufferSize = 64 * 1024
    password = "bbbo-02-21"

#True-зашифровать
#False-расшифровать

    with open(filename, "rb") as f:
        file_content = io.BytesIO(f.read())

    with open(filename, "wb") as f:
        if is_encrypted:
            pyAesCrypt.encryptStream(
                file_content,
                sequence_bytes,
                password,
                bufferSize
            )
        else:
            pyAesCrypt.decryptStream(
                file_content,
                sequence_bytes,
                password,
                bufferSize,
                len(file_content.getvalue())
            )
        f.write(sequence_bytes.getvalue())

def create():
    path = pathlib.Path('log.log')
    if path.exists() == True:
        MemoryCrypter("log.log", False)
        with open('log.log') as file:
            array = [row.strip() for row in file]
        word = "ERROR"
        path = pathlib.Path('otchet.log')
        if path.exists() == True:
            for i in array:
                for word in i:
                    f = open("otchet.log", "a")
            f.write(i)
            MemoryCrypter("log.log",True)
        else:
            for i in array:
                for word in i:
                    f = open("otchet.log", "w+")
            f.write(i+"\n")
            MemoryCrypter("log.log", True)
def thr():
    while True:
        schedule.run_pending()

class DEBUG:
    def __init__(self,message):
        level = "DEBUG"
        vremya = str(datetime.datetime.now())
        stw ="['date' : " + vremya + ": " + level + "]" +" "+message+"\n"
        path = pathlib.Path('log.log')
        if path.exists() == True:
            MemoryCrypter("log.log", False)
            my_file = open("log.log", "a")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log", True)
        else:
            my_file = open("log.log", "w+")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log",True)
        print(stw)

class INFO:
    def __init__(self,message):
        level = "INFO"
        vremya = str(datetime.datetime.now())
        stw = "['date' : " + vremya + ": " + level + "]" +" "+message+"\n"
        path = pathlib.Path('log.log')
        if path.exists()==True:
            MemoryCrypter("log.log", False)
            my_file = open("log.log", "a")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log", True)
        else:
            my_file = open("log.log", "w+")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log", True)
        print(stw)

class ERROR:
    def __init__(self,message):
        level = "ERROR"
        vremya = str(datetime.datetime.now())
        stw = "['date' : " + vremya + ": " + level + "]" +" "+message+"\n"
        path = pathlib.Path('log.log')
        if path.exists() == True:
            MemoryCrypter("log.log", False)
            my_file = open("log.log", "a")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log", True)
        else:
            my_file = open("log.log", "w+")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log", True)
        print(stw)

class CREATE_pdf:
    def __init__(self,N):
        tilt = N
        schedule.every(tilt).hours.do(create)
        threading.Thread(target=thr).start()

class SORTBY:
    def __init__(self,mod):
        print("mods: sort_by_level sort_by_time first_n last_n")
        if mod =="sort_by_level":
            path = pathlib.Path('log.log')
            if path.exists() == True:
                MemoryCrypter("log.log", False)
                with open('log.log') as file:
                    array = [row.strip() for row in file]
                    print("vvedite level\n")
                    word = input()
                    for i in array:
                        if word in i:
                            print(i)
                file.close()
                MemoryCrypter("log.log", True)

        if mod =="sort_by_time":
            path = pathlib.Path('log.log')
            if path.exists() == True:
                path = pathlib.Path('log.log')
                if path.exists() == True:
                    MemoryCrypter("log.log", False)
                    print("vvedite n\n")
                    n = int(input())
                    print("vvedite m\n")
                    m = int(input())
                    with open("log.log") as file:
                        array = [row.rstrip() for row in file]
                    for line in array:
                        while True:
                            true_line = line
                            time_str = line[21] + line[22]
                            time = (sum(map(int, time_str.split())))
                            if ((time >= n) and (time <= m)) or (time == n) or (time == m):
                                print(true_line)
                                file.close()
                                MemoryCrypter("log.log", True)
                                break
                            else:
                                file.close()
                                MemoryCrypter("log.log", True)
                                break

        if mod =="first_n":
            path = pathlib.Path('log.log')
            if path.exists() == True:
                path = pathlib.Path('log.log')
                if path.exists() == True:
                    MemoryCrypter("log.log", False)
                    print("input n")
                    n = int(input())
                    with open("log.log", 'r') as f:
                        for i in range(n):
                            print(f.readline())
                    f.close()
                    MemoryCrypter("log.log", True)

        if mod == "last_n":
            path = pathlib.Path('log.log')
            if path.exists() == True:
                path = pathlib.Path('log.log')
                if path.exists() == True:
                    MemoryCrypter("log.log", False)
                    print("input n\n")
                    n = int(input())
                    from collections import deque
                    with open("log.log") as f:
                        for row in deque(f, n):
                            print(row.strip())
                    f.close()
                    MemoryCrypter("log.log", True)
