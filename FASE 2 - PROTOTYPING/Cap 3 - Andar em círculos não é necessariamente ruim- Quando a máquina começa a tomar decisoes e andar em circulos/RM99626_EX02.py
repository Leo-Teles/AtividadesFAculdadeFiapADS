print(" Qual seria o melhor dia para realização das lives? ")

segundaFeira = int(input("qual foi a quantidade de votos segunda-feira?"))
terçaFeira = int(input("qual foi a quantidade de votos terça-feira?"))
quartaFeira = int(input("qual foi a quantidade de votos quarta-feira?"))
quintaFeira = int(input("qual foi a quantidade de votos quinta-feira?"))
sextaFeira = int(input("qual foi a quantidade de votos sexta-feira?"))

if segundaFeira > terçaFeira and segundaFeira > quartaFeira and segundaFeira > quintaFeira and segundaFeira > sextaFeira:
    print(" Segunda-feira foi escolhido como dias das lives com {} votos".format(segundaFeira))

if terçaFeira > segundaFeira and terçaFeira > quartaFeira and terçaFeira > quintaFeira and terçaFeira > sextaFeira:
    print(" Terça-feira foi escolhido como dias das lives com {} votos".format(terçaFeira))

if quartaFeira > segundaFeira and quartaFeira > terçaFeira and quartaFeira > quintaFeira and quartaFeira > sextaFeira:
    print(" Quarta-feira foi escolhido como dias das lives com {} votos".format(quartaFeira))

if quintaFeira > segundaFeira and quintaFeira > terçaFeira and quintaFeira > quartaFeira and quintaFeira > sextaFeira:
    print(" Quinta-feira foi escolhido como dias das lives com {} votos".format(quintaFeira))

if sextaFeira > segundaFeira and sextaFeira > terçaFeira and sextaFeira > quartaFeira and sextaFeira > quintaFeira:
    print(" Sexta-feira foi escolhido como dias das lives com {} votos".format(sextaFeira))