class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
carros = []

while True:
    mod = input("Moldelo do carro (0 para finalizar): ")
    if mod == '0':
        break
    ano = input("Ano do carro: ")
    carro = Car(mod, ano)
    carros.append(carro)

dicionario = {}

for i, carro in enumerate(carros, start=1):
    dicionario[f"Carro {i}"] = {'Modelo: ': carro.model, "Ano: ":carro.year}

print(dicionario)