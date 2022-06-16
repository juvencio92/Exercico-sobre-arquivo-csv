
import csv

mostrar_dados = csv.reader(open("dados.csv"), delimiter=",")

for [nome, idade, genero] in mostrar_dados:
    print("{} tem {} anos de idade e {}\n".format(nome, idade, genero))
