class Disciplina:
    def __init__(self, nome, semestre, media, ch):
        self.__nome = nome
        self.__semestre = semestre
        self.__media = media
        self.__ch = ch
        self.__aprovado = media >= 60


    def getSemestre(self):
        return self.__semestre

    def getMedia(self):
        return self.__media


    def __str__(self):
        if self.__aprovado:
            return f'{self.__nome} --> {self.__semestre} --> {self.__ch} = aprovado com média de {self.__media}'
        else:
            return f'{self.__nome} --> {self.__semestre} --> {self.__ch} = reprovado com média de {self.__media}'
        

class Historico: 
    def __init__(self, aluno):
        self.__aluno = aluno
        self.__disciplinas = []

    def inserir(self, disc):
        self.__disciplinas.append(disc)
    
    def listar(self): #igual a get
        return self.__disciplinas
    
    def listar_semestre(self, semestre):
        x = []
        for disc in self.__disciplinas:
            if disc.getSemestre() == semestre:
                x.append(disc)
        return x


    def IRA(self):
        if len(self.__disciplinas) == 0: return 0
        soma = 0
        for disc in self.__disciplinas:
            soma += disc.getMedia()
        return soma / len(self.__disciplinas)
        

####################################################

h = Historico('aluno')
a = Disciplina("POO", "2024.1", 100, 90)
b = Disciplina("Algoritmos", "2024.1", 100, 55)
c = Disciplina("Inglês", "2023.1", 90, 80)

h.inserir(a)
h.inserir(b)
h.inserir(c)

print("Todas as disciplinas")
print(*h.listar())

for disc in h.listar():
    print(disc)

for disc in h.listar_semestre("2024.1"):
    print(disc)

print(a)
print(b)
print(c)

print(h.IRA())