import csv
from exercicios.ex22 import 

with open("grid.csv", "r") as arquivo:
    csv_writer = csv.writer(arquivo, delimiter=",")
