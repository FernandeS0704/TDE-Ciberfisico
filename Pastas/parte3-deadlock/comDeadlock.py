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
    lock_B.acquire()
    print("[Thread 2] Iniciou, tem: Lock B")

    time.sleep(0.05)

    lock_A.acquire()
    print("[Thread 2] tem: Lock A!")

    print("Thread 2] encerrou: SUCESSO")
    lock_A.release()
    lock_B.release()

# para mostrar o estado de cada thread
def monitor_sistema():
    time.sleep(2)
    print("\n--- DIAGNÓSTICO DO SISTEMA ---")
    for t in threading.enumerate():
        if t != threading.current_thread() and t.name != "MainThread":
            print(f"Status da {t}: BLOQUEADA (Aguardando liberação de lock)")
    print("\n--- O programa travou em Deadlock ---")

# Inicialização das Threads
t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)
monitor = threading.Thread(target=monitor_sistema, name="Monitor")

t1.start()
t2.start()
monitor.start()
