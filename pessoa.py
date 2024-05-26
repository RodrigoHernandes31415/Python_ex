class person:
    def __init__(self, name, nick, age):
        self.name = name
        self.nick = nick
        self.age = age

nome = str(input("Qual seu nome: "))
sobN = str(input("Qual seu sobrenome: "))
idade = int(input("Qual sua idade: "))

pessoa = person(nome, sobN, idade)
print("Seu nome é {} {} e você tem {} anos".format(pessoa.name,pessoa.nick, pessoa.age))