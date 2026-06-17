import threading
import time


THREADS_TOTAL = 8      
INCREMENTOS_TOTAL = 200000  

contador_global = 0    
semaforo_binario = threading.Semaphore(1)  


def tarefa_sem_sincronizacao():
    global contador_global
    for _ in range(INCREMENTOS_TOTAL):
        atual = contador_global
        
        time.sleep(0)
        
        contador_global = atual + 1

def tarefa_com_semaforo():
    global contador_global
    for _ in range(INCREMENTOS_TOTAL):
        semaforo_binario.acquire()
        try:
            
            atual = contador_global
            time.sleep(0)  
            contador_global = atual + 1
        finally:
            semaforo_binario.release()

def rodar_experimento(funcao_alvo):
    global contador_global
    contador_global = 0  
    
    lista_de_threads = []
    
    for _ in range(THREADS_TOTAL):
        t = threading.Thread(target=funcao_alvo)
        lista_de_threads.append(t)
        
    tempo_inicio = time.time()
    
    for t in lista_de_threads:
        t.start()
        
    for t in lista_de_threads:
        t.join()
        
    tempo_fim = time.time()
    tempo_total = tempo_fim - tempo_inicio
    
    return contador_global, tempo_total

if __name__ == "__main__":
    valor_esperado = THREADS_TOTAL * INCREMENTOS_TOTAL
    print(f"T = {THREADS_TOTAL} threads, M = {INCREMENTOS_TOTAL} incrementos")
    print(f"Valor final esperado (T * M): {valor_esperado}")
    
    print("Executando a versão sem sincronização")
    resultado_sem, tempo_sem = rodar_experimento(tarefa_sem_sincronizacao)
    print(f"Resultado: {resultado_sem}")
    print(f"Tempo gasto: {tempo_sem:.4f} segundos")
    print(f"Perda de incrementos: {valor_esperado - resultado_sem}")
    
    print("-----------------------------------------------------")
    
    print("Executando a versão com Semáforo Binário")
    resultado_com, tempo_com = rodar_experimento(tarefa_com_semaforo)
    print(f"Resultado: {resultado_com}")
    print(f"Tempo gasto: {tempo_com:.4f} segundos")
    print(f"Diferença do esperado: {valor_esperado - resultado_com}")