from multiprocessing import Process
import os


def start_httpserver():
    os.system("python httpserver.py")
    print("http服务启动完成 ...")


def start_playserver():
    os.system("python playserver.py")
    print("语言合成服务启动完成 ...")


if __name__ == "__main__":
    """
    #print('Parent process %s.' % os.getpid())
    #p = Process(target=start_httpserver)
    # p = Process(target=start_httpserver, args=(voice,))
    # p.start()
    # p.join()
    """
    p = Process(target=start_playserver)
    p.start()
    p.join()
    print('进程结束 ...')

