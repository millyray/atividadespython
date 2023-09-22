perguntas=["está chovendo?" , "você vai assistir aula hoje?" ,"lavou os pratos", "conseguiu dormir direito?", "já comeu hoje?", "bebeu água?", "você gosta de estudar do SESI?", "praticou exercícios hoje?", "gosta de chocolate?", "gosta de lasanha?"]
respostas=["sim", "talvez", "não","não", " sim","sim", "sim" , " não", "sim", "sim"]

nota=0

for i in range(10):
    x= input(perguntas[i])
    if x==respostas[i]:
        print("acertou!")
        nota+=1
    else:
        print(" errou otário!")

if nota==0:
    print(f"sua nota foi {nota}"),
else:
    print(f"sua nota foi {nota}")
