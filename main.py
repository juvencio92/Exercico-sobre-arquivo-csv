
import csv

mostrar_dados = csv.reader(open("dados.csv"), delimiter=",")

for [nome, idade, genero] in mostrar_dados:
    print("{} tem {} anos de idade e {}\n".format(nome, idade, genero))

###################### OUTRA FORMA ##############################

with open("dados.csv", "r") as arq:
    leitura = csv.reader(arq, delimiter=",")
    for [nome, idade, genero] in leitura:
        print("{} is {} years old and {} ".format(nome, idade,genero))
