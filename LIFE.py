from random import randint
from time import sleep

#FONTES:
#https://www.uol.com.br/vivabem/noticias/bbc/2018/04/20/beber-alcool-todo-dia-reduz-expectativa-de-vida-aponta-estudo-britanico.html
#https://www.hospitalsiriolibanes.org.br/sua-saude/Paginas/Tabagismo-diminui-expectativa-de-vida-em-mais-de-10-anos.aspx#:~:text=Estudos%20indicam%20que%20o%20tabagismo,fumar%22%2C%20avalia%20o%20dr.
#https://www.jcnet.com.br/noticias/geral/2012/11/359614-sedentarismo-ja-ameaca-longevidade.html
#https://gauchazh.clicrbs.com.br/saude/vida/noticia/2014/12/Beber-refrigerante-pode-diminuir-4-6-anos-de-vida-4655893.html


print('ESTE PROGRAMA FOI BASEADO EM ESTUDOS SOBRE O CONSUMO EXCESSIVO DE SUBSTANCIAS E HABITOS QUE PODEM REDUZIR A LONGEVIDADE DA VIDA HUMANA.')
sleep(3)
genero = int(input('selecione seu sexo\n[0]Homem\n[1]Mulher\n'))

while True:
    def LIFE():
        if genero == 0:
            idadeh = int(input('qual a sua idade ?'))
            idademediabrh = 76
            idaderestantteh = idademediabrh - idadeh

            questfh = str(input('é fumante ?\n[S] Sim\n[N] Não')).upper()
            if questfh == 'S':
                fumo = idaderestantteh - 12
            if questfh == 'N':
                fumo = idaderestantteh - 0

            questah = str(input('Consome alcool ?\n[S] sim\n[N] não')).upper()
            if questah == 'S':
                alcool = fumo - 5
            if questah == 'N':
                alcool = fumo - 0

            questsh = str(input('é sedentario ?\n[S] sim\n[N]não')).upper()
            if questsh == 'S':
                sedent = alcool - randint(3, 5)
            if questsh == 'N':
                sedent = alcool - 0

            questrefri = str(input('Consome refrigerantes ?\n[S] sim\n[N]nao\n')).upper()
            if questrefri == 'S':
                refri = sedent - randint(4, 6)
            if questrefri == 'N':
                refri = sedent - 0

            print(f'Te resta {refri} anos ')
            viver = idadeh + refri
            print(f'voce provavelmente viverá em torno dos {viver} anos')

        if genero == 1:
            idadem = int(input('qual a sua idade ?'))
            idademediabrm = 79
            idaderestanttem = idademediabrm - idadem

            questfm = str(input('é fumante ?\n[S] Sim\n[N] Não')).upper()
            if questfm == 'S':
                fumom = idaderestanttem - 11
            if questfm == 'N':
                fumom = idaderestanttem - 0

            questam = str(input('Consome alcool ?\n[S] sim\n[N] não')).upper()
            if questam == 'S':
                alcoolm = fumom - 5
            if questam == 'N':
                alcoolm = fumom - 0

            questsm = str(input('é sedentario ?\n[S] sim\n[N]não')).upper()
            if questsm == 'S':
                sedentm = alcoolm - randint(3, 5)
            if questsm == 'N':
                sedentm = alcoolm - 0

            questrefrim = str(input('Consome refrigerantes ?\n[S] sim\n[N]nao\n')).upper()
            if questrefrim == 'S':
                refrim = sedentm - randint(4, 6)
            if questrefrim == 'N':
                refrim = sedentm - 0

            print(f'Te resta {refrim} anos ')
            viverm = idadem + refrim
            print(f'voce provavelmente viverá em torno dos {viverm} anos')

    LIFE()

    def reboot():
        perg = str(input('Deseja fazer mais uma consulta?\n[S] para sim\n[N]para não')).upper()
        if perg =='S':
            LIFE()
        else:
            print('sair')

    reboot()
