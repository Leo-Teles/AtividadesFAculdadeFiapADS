# 4 – Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado por um software malicioso que criptografou todos os discos e pede a digitação de uma senha para a liberação da máquina. E é claro que os criminosos exigem um pagamento para informar a senha.

#Ao analisar o código do programa deles, porém, você descobre que a senha é composta pela palavra “LIBERDADE” seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120). Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio. ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do fatorial. Ele deve obrigatoriamente utilizar loop.

nova_resposta = 0

resposta = int(input("Digite os minutos desse extato momneto: "))
nova_resposta = resposta -1


for fatorial in range(1, resposta, 1):
    atual = resposta * nova_resposta
    resposta = atual
    nova_resposta = nova_resposta - 1
    print(atual)

print("A senha é {}". format(atual))

