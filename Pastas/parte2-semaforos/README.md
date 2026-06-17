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


Por que a versão sem sincronização perde incrementos?

Porque a operação de ler e atualizar o contador não acontece de uma vez na CPU. Basicamente o processo é dividído em 3 etapas, ler o valor atual da memória, somar 1 na CPU e gravar o resultado de volta. Enquanto a thread 1 está pausada segurando um valor antigo (tipo 100), as threads 2,3,4 entram, leem o mesmo valor 100, somam 1 e gravam 101. Quando a thread 1 "acorda", ela também grava 101. No fim das contas várias threads trabalharam, mas o contador só subiu uma vez (Race COndition).

A outra versão usamos acquire(), ela "tranca a porta" da seção crítica. Mesmo que ocorra a troca de ordem pelo time.sleep(0), nenhuma outra thread conseguirá ler ou modificar o contador_global, pois todas ficarão bloqueadas na linha do acquire() aguardando sua vez. Apenas quando a thread atual finaliza a escrita e executa o release(), a próxima da fila pode entrar. Isso garante que a operação de incremento aconteça corretamente.

A demora da versão com semáforo é bem maior, por causa do overhead de sincronização. O sistema e o interpretador de python gastam muito mais tempo controlando a fila do semáforo, bloqueando as threads, acordando threads e fazendo trocas de ordem. O throughput cai muito, esse é o preço necessário para garantir que o resultado final não seja perdido.

As CPUs modernas possuem memórias cache locais muito rápida. Sem sincronização, uma thread poderia alterar o valor do contador na sua própria cache e demorar para atualizar a memória principal, fazendo com que as outras threads continuassem lendo dados velhos. Quando usamos os métodos acquire() e release() do módulo threading, o python cria barreiras implícitas de hardware, elas forçam o computador a publicar imediatamente qualquer alteração na memória na linha principal antes que outra thread possa adquirir o semáforo, garantindo visibilidade total e uma ordem cronológica perfeita das operações.

Realizei teste com código sem o time.sleep(0) e os resultados eram sempre iguais sem perdas de ambos os lados devido a velocidade do processador, dessa forma (utilizando)  "forçamos" o sistema a alternar as threads logo após a leitura da variável global.

