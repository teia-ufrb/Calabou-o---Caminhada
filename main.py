# Trilha com Barreiras
import random
import time
MAX_REPETIÇÕES = 100 * 1000

### Caminhada ###
def Caminhada():
    TotalJogadas = 0

    for tentativa in range(1, MAX_REPETIÇÕES+1):
        TamanhoPercurso = 27
        Barreiras = [9, 18, 27, 0]
        PosiçãoAtual = 0
        BarreiraAtual = 0
        Jogadas =0

        while PosiçãoAtual < TamanhoPercurso :
            Deslocamento = int(random.randrange(1,7))
            #print(PosiçãoAtual,TamanhoPercurso, Deslocamento, BarreiraAtual)
            if( PosiçãoAtual+Deslocamento <= Barreiras[BarreiraAtual] ):
                PosiçãoAtual= PosiçãoAtual + Deslocamento
                if(PosiçãoAtual == Barreiras[ BarreiraAtual ]):
                    BarreiraAtual = BarreiraAtual + 1
            Jogadas = Jogadas +1

        TotalJogadas = TotalJogadas + Jogadas

    return (TotalJogadas/MAX_REPETIÇÕES)


### Main ###
print(" *** Trilha com Barreiras *** ")

#Solotário
print("Quantas Jogadas são necessárioas para chegar ao fim do percurso?")
t_inicio = time.time()
Passos = Caminhada()
print(Passos, "Jogadas")
print("Segundos:", time.time() - t_inicio)
