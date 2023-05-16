#Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

#Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas, deve ser exibida uma mensagem no seguinte padrão:

#VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

#POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

notaPar = 0
notaImpar = 0

print("NOTAS ALUNOS PARES")
for Par in range (2, 51, 2):

    nota = int(input("Digite a nota do aluno Nº{} PAR:".format(Par)))
    notaPar = notaPar + nota

print("NOTAS AULUNOS IMPARES")
for Impar in range (1, 50, 2):

    nota = int(input("Digite a nota do aluno Nº{} IMPAR: ".format(Impar)))
    notaImpar = notaImpar + nota

print("MÈDIA DOS ALUNOS INPARES E PARES")
mediaPar = notaPar / 25
print(" A nota media dos números pares é {}".format(mediaPar))

mediaImpar = notaImpar /25
print(" A nota media dos números impares é {}".format(mediaImpar))


print("QUEM FICOU COM MAIOR MÈDIA ENTRE IMPARES E PARES")
if mediaPar > mediaImpar:
    print("A media dos alunos pares é maior que dos alunos pares com {}".format(mediaPar))

elif mediaImpar > mediaPar:
    print("A media dos alunos impares é maior que dos alunos pares com {}".format(mediaImpar))


