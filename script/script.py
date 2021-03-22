from selenium.webdriver import Firefox
from time import sleep 
import pandas as pd 
import numpy as np 

url = 'https://interativos.globoesporte.globo.com/esports/lol/tabela-cblol/2021'
browser = Firefox()
browser.get(url)

main = browser.find_element_by_tag_name('main')
botao1 = main.find_element_by_class_name('arrow-wrapper--prev')
botao1.click()
sleep(2)

tabela = main.find_element_by_class_name('tabela-jogos')
rod = tabela.find_element_by_class_name('carousel__title')
rodada = int(rod.text.split()[0].replace('ª',''))

botaoesq = tabela.find_element_by_class_name('arrow-wrapper--prev')
botaodir = tabela.find_element_by_class_name('arrow-wrapper--next')

Clear = lambda a: a.clear()

for i in range(rodada):
    try:
        botaoesq.click()
        sleep(0.5)
    except:
        break

t1 = []
r1 = []
r2 = []
t2 = []

tt1 = []
rr1 = []
rr2 = []
tt2 = []

for j in range(rodada):
    for i in range(5):
        cc = tabela.find_element_by_class_name('carousel__content')
        ul = cc.find_element_by_class_name('carousel__content-list')
        lis = ul.find_elements_by_tag_name('li')
        jogo = lis[i].find_element_by_tag_name('div')
        placar = jogo.find_element_by_class_name('game-placcard')
        times = placar.find_elements_by_class_name('game-placcard__team')
        time1 = times[0].find_element_by_tag_name('p')
        time2 = times[1].find_element_by_tag_name('p')
        resultados = placar.find_element_by_class_name('game-placcard__result')
        resultadot1 = resultados.find_element_by_class_name('game-placcard__result--team-a')
        resultadot2 = resultados.find_element_by_class_name('game-placcard__result--team-b')
        Clear(times)
        t1.append(time1.text)
        t2.append(time2.text)
        r1.append(resultadot1.text)
        r2.append(resultadot2.text)

    try:           
        botaodir.click()
        sleep(0.3)
    except:
        break 

if rodada < 18:
    for j in range(18-rodada):
        for i in range(5):
            cc = tabela.find_element_by_class_name('carousel__content')
            ul = cc.find_element_by_class_name('carousel__content-list')
            lis = ul.find_elements_by_tag_name('li')
            jogo = lis[i].find_element_by_tag_name('div')
            placar = jogo.find_element_by_class_name('game-placcard')
            times = placar.find_elements_by_class_name('game-placcard__team')
            time1 = times[0].find_element_by_tag_name('p')
            time2 = times[1].find_element_by_tag_name('p')
            resultados = placar.find_element_by_class_name('game-placcard__result')
            resultadot1 = resultados.find_element_by_class_name('game-placcard__result--team-a')
            resultadot2 = resultados.find_element_by_class_name('game-placcard__result--team-b')
            Clear(times)
            tt1.append(time1.text)
            tt2.append(time2.text)
            rr1.append(resultadot1.text)
            rr2.append(resultadot2.text)

        if True:
            try:             
                botaodir.click()
                sleep(0.3)
            except:
                break
     
    jf = np.array([tt1,rr1,rr2,tt2])
    jf = jf.transpose()
    dfjf = pd.DataFrame(jf,columns = ["Home","X","Y","Visitor"])
    print(dfjf)
    dfjf.to_csv('jf.csv',sep=str(','),index = False)




bdd = np.array([t1,r1,r2,t2])
bdd = bdd.transpose()
dfbdd = pd.DataFrame(bdd,columns = ["Home","X","Y","Visitor"])
dfbdd.to_csv('bdd.csv',sep=str(','),index = False)
browser.quit()