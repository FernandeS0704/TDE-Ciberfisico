import threading
import time

lock_A = threading.Lock()
lock_B = threading.Lock()

def thread_1():
    lock_A.acquire()
    print("[Thread 1] Iniciou, tem: Lock A")

    time.sleep(0.05)

    lock_B.acquire()
    print("[Thread 1] tem: Lock B!")

    print("[Thread 1] encerrou: SUCESSO")
    lock_B.release()
    lock_A.release()

def thread_2():
    print("[Thread 2] buscando Lock A")
    lock_A.acquire()
    print("[Thread 2] Iniciou, tem: Lock A")

    time.sleep(0.05)

    print("[Thread 2] buscando Lock B...")
    lock_B.acquire()
    print("[Thread 2] tem: Lock B")

    print("[Thread 2] encerrou: SUCESSO")
    lock_B.release()
    lock_A.release()


t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()
