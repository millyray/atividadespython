#exemplo de givaneo 
name = ['Jessa' , 'Eric' , 'bob']
filename = "meuAquivo.txt"
file = open(filename, 'w')
for name in name:
    file.write("%s\n" % name)
file.close()

print("alteração")