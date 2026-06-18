# TDE-Ciberfisico

# Nome do Grupo: CyberCode

# Integrantes: 
- Arthur de Almeida Fernandes
- Josue Aurelio Nonalaya Vilca
- Pedro Henrique Borges Odia

# Linguagem escolhida:
- Python
#URL video Youtube

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
