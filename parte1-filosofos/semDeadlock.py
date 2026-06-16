import threading
import time
import os

filosofos = ["F1", "F2", "F3", "F4", "F5"]
estado = ["Pensando"] * 5
garfos = [threading.Lock() for _ in range(5)]
lock_estado = threading.Lock()


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_estado():
    limpar_tela()
    print("JANTAR DOS FILÓSOFOS\n")
    for i, f in enumerate(filosofos):
        print(f"{f}: {estado[i]}")
    print("\nCtrl+C para sair")


def atualizar(i, novo_estado):
    with lock_estado:
        estado[i] = novo_estado
        mostrar_estado()


def filosofo(i):
    esquerda = i
    direita = (i + 1) % 5

    while True:
        atualizar(i, "Pensando")
        time.sleep(1)

        atualizar(i, "Com fome")

        primeiro = min(esquerda, direita)
        segundo = max(esquerda, direita)

        garfos[primeiro].acquire()
        garfos[segundo].acquire()

        atualizar(i, "Comendo")
        time.sleep(2)

        garfos[segundo].release()
        garfos[primeiro].release()


for i in range(5):
    threading.Thread(target=filosofo, args=(i,), daemon=True).start()

while True:
    time.sleep(1)