import threading
import time
import os

filosofos = ["F1", "F2", "F3", "F4", "F5"]
garfos = [threading.Lock() for _ in range(5)]

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def filosofo(i):
    esquerda = i
    direita = (i + 1) % 5

    while True:
        print(f"{filosofos[i]} Pensando")
        time.sleep(1)

        print(f"{filosofos[i]} Com fome")

        garfos[esquerda].acquire()

        time.sleep(0.1)
        garfos[direita].acquire()
        print(f"{filosofos[i]} Comendo")
        time.sleep(2)

        garfos[direita].release()
        garfos[esquerda].release()


for i in range(5):
    threading.Thread(target=filosofo, args=(i,), daemon=True).start()

while True:
    time.sleep(1)