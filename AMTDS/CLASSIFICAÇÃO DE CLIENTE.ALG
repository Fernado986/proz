Algoritmo "Classificação de Cliente"
Var
   nome, categoria: caracter
   valor: real

Inicio
escreva("Informe seu nome: ")
leia(nome)

escreva("Informe o valor total de compras do último ano: ")
leia(valor)

se valor <= 1000 entao
   categoria <- "BRONZE"
senao
    se valor <= 5000 entao
        categoria <- "PRATA"
    senao
       se valor <= 10000 entao
           categoria <- "OURO"
       senao
           categoria <- "DIAMANTE"
       fimse
    fimse
fimse

escreva(nome, ", sua categoria é: ", categoria)


Fimalgoritmo
