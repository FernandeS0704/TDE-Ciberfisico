# TDE-Ciberfisico

# Nome do Grupo: CyberCode

# Integrantes: 
- Arthur de Almeida Fernandes
- Josue Aurelio Nonalaya Vilca
- Pedro Henrique Borges Odia

# Linguagem escolhida:
- Python
  
# URL video Youtube

# Instruções de compilação e execução
- Requisitos: Python 3.10+

- Passos
    1.Clonar o repositório
git clone https://github.com/FernandeS0704/TDE-Ciberfisico.git
    2.Acesse as pastas do projeto
cd TDE_Ciberfisico
cd Pastas (escolha a parte do projeto q vc quer rodar)
cd parte1-filosofos
    3.Execute o Arquivo Python
python semDeadlock.py


# Relatórios Técnicos 
# Parte 1
- Dinamica do problema
O jantar dos filosofos é um classico problema de algorítimos concorrentes na computação, onde cinco filosofos estão sentados em uma mesa com um prato no meio com comida. O dilema acontece já que cada filosofo precisa de dois garfos para comer e existem 5 garfos sobre a mesa e s filosofos podem escolher "pensar", "pegar" um garfo (da esquerda ou o da direita) e "comer".

- Impasse
Como dito, para comer precisam de dois garfos, porém, o que pode acontecer é todos escolherem o da esquerda ao mesmo tempo, assim, cada filosofo ficaria aguardando um segundo garfo que ninguém vai conseguir pegar devido a todos estarem esperando ficar livre. Dessa forma, ocorreria um problema no sistema e travaria, o chamado "Deadlock".

- Codições de Coffman
Estas quatro condições são necessárias para que ocorra um impasse:
Exclusão mútua (nenhum garfo pode ser usado simultaneamente por vários filósofos)
Detenção de recursos (os filósofos seguram um garfo enquanto esperam pelo segundo)
Não-preempção (nenhum filósofo pode pegar um garfo de outro)
Espera circular (cada filósofo pode estar esperando pelo filósofo à sua esquerda)

- Solução
A condição de Coffman que será negada para solução do problema é a Espera Circular, onde para resolver o problema vamos colocar uma regra para que o filósofo pegue sempre o garfo de menor indice. Assim evitando o problema de todos escolherem esquerda

- Fluxograma
Garfos liberados:
Thread criada -> entra em filosofo(0) -> define grafos (garfo[0] e garfo[1]) -> pesando -> com fome -> pega garfos -> comendo -> devolve garfos 
Garfos sendo usados:
Thread criada -> entra em filosofo(0) -> define grafos (garfo[0] e garfo[1]) -> pesando -> com fome -> tenta pegar garfos -> espera garfos serem liberados -> pega garfos -> comendo -> devolve garfos

# Parte 2
Por que a versão sem sincronização perde incrementos?

Porque a operação de ler e atualizar o contador não acontece de uma vez na CPU. Basicamente o processo é dividído em 3 etapas, ler o valor atual da memória, somar 1 na CPU e gravar o resultado de volta. Enquanto a thread 1 está pausada segurando um valor antigo (tipo 100), as threads 2,3,4 entram, leem o mesmo valor 100, somam 1 e gravam 101. Quando a thread 1 "acorda", ela também grava 101. No fim das contas várias threads trabalharam, mas o contador só subiu uma vez (Race COndition).

A outra versão usamos acquire(), ela "tranca a porta" da seção crítica. Mesmo que ocorra a troca de ordem pelo time.sleep(0), nenhuma outra thread conseguirá ler ou modificar o contador_global, pois todas ficarão bloqueadas na linha do acquire() aguardando sua vez. Apenas quando a thread atual finaliza a escrita e executa o release(), a próxima da fila pode entrar. Isso garante que a operação de incremento aconteça corretamente.

A demora da versão com semáforo é bem maior, por causa do overhead de sincronização. O sistema e o interpretador de python gastam muito mais tempo controlando a fila do semáforo, bloqueando as threads, acordando threads e fazendo trocas de ordem. O throughput cai muito, esse é o preço necessário para garantir que o resultado final não seja perdido.

As CPUs modernas possuem memórias cache locais muito rápida. Sem sincronização, uma thread poderia alterar o valor do contador na sua própria cache e demorar para atualizar a memória principal, fazendo com que as outras threads continuassem lendo dados velhos. Quando usamos os métodos acquire() e release() do módulo threading, o python cria barreiras implícitas de hardware, elas forçam o computador a publicar imediatamente qualquer alteração na memória na linha principal antes que outra thread possa adquirir o semáforo, garantindo visibilidade total e uma ordem cronológica perfeita das operações.

Realizei teste com código sem o time.sleep(0) e os resultados eram sempre iguais sem perdas de ambos os lados devido a velocidade do processador, dessa forma (utilizando)  "forçamos" o sistema a alternar as threads logo após a leitura da variável global.

T = 8 threads, M = 200000 incrementos
Valor final esperado (T * M): 1600000


Versão em sincronização
Resultado: 200168
Tempo gasto: 2.4768 segundos
Perda de incrementos: 1399832

Versão com Semáforo Binário
Resultado: 1600000
Tempo gasto: 14.8053 segundos
Diferença do esperado: 0


-----------------------------------------------------

Versão sem sincronização
Resultado: 200032
Tempo gasto: 2.3525 segundos
Perda de incrementos: 1399968

Versão com Semáforo Binário
Resultado: 1600000
Tempo gasto: 15.2908 segundos
Diferença do esperado: 0

-----------------------------------------------------

Versão sem sincronização:
Resultado: 200249
Tempo gasto: 2.4901 segundos
Perda de incrementos: 1399751

Versão com Semáforo Binário:
Resultado: 1600000
Tempo gasto: 14.8350 segundos
Diferença do esperado: 0

# Parte 3
- O Deadlock foi produzido porque a thread1 inicia pegando por primeiro o lock A, apos uma breve pausa, a thread2 segura o lock B. A segunda parte de cada thread requerem o lock que a contraria possui, cada uma deberia liberar a atual, mas isso não é possivel pois ambos locks estao sendo usados ao mesmo tempo.

- As condições de Coffman que acontecem nesta parte sao as 4: exclusao mutua(ambos os locks sao somente possiveis de ser detidos uma thread por vez), manter-e-esperar(ambas as threads mantem o lock que possuem priemiro e aguardam o segundo ser liberado porem nao será), não preempção(a liberação precisa ser voluntaria de cada thread) e espera circular(forma se um ciclo circular de dependencia entre ambas as threads).

- A solução utilizada foi a prevenção através de impor uma hierarquia de recursos. Foi tirado a ordem cruzada de execução ao pegar os locks, e se definiu que o lock A sempre deve ser adquirido antes do B, assim quebrando o problema da espera circular.


# Prints de Execução

# Parte 1

## Execução Inicial

(imagens/execucao1.png)

## Execução Normal

(imagens/execucao2.png)

## Execução com Deadlock

(imagens/execucao3.png)

# Parte 3
 Execução com Deadlock(comDeadlock.py) 
 - (imagens/comDeadlock.JPG)

 Execução corregida(semDeadlock.py)
- (imagens/semDeadlock.JPG)
