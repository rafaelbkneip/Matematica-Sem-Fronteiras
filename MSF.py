import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import pdfplumber
from PyPDF2 import PdfReader

import save

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ['enable-automation'])

navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)
navegador2 = webdriver.Chrome(ChromeDriverManager().install(), options=options)
navegador.get("http://www.matematicasemfronteiras.org/resultados_nacionais2022.html")

unica = []
aux_list = []

medalhas = []

controle = True
cont = 0

while(controle):

    cont = cont + 1
     
    try:
        pdf = navegador.find_element(By.XPATH, '//*[@id="navtres"]/ul/li['+str(cont)+']/a').get_attribute('href')

        navegador2.get(pdf)

        try:
            r = requests.get(pdf, stream=True)
            with open('Resultados'+str(cont)+'.pdf', 'wb') as f:
                    for chunk in r.iter_content():
                        f.write(chunk)
        except:
            print("Erro")

        pdf = pdfplumber.open() 
        readpdf = PdfReader()

        unica = []

        print("O arquivo possui", len(readpdf.pages), "páginas")

        for j in range(len(readpdf.pages)):
            text = pdf.pages[j].extract_text()
            listas = text.split("\n")
            unica = unica + listas

        premiacao = unica[0]

        unica.pop(0)
        unica.pop(0)

        for linha in range(len(unica)):

            teste = unica[linha]

            aux_list_name = []
            print(teste)

            aux = ''

            splitted = teste.split(" ")

            #SIGLA
            aux_list.append(teste.split(" ")[0])

            #MUNICIPIO
            for i in range(1, len(splitted)):
                if(splitted[i].isupper() == False):
                    aux_list_name.append(splitted[i])
                    aux_list_name.append(" ")

                else:
                    comeco = i
                    break

            for text in range(len(aux_list_name)-1):
                aux = aux + aux_list_name[text]

            aux_list.append(aux)
            aux_list_name = []
            aux = ''

            #ESCOLA
            for j in range(comeco, len(splitted)):
                if(splitted [j].isupper() == True):
                    aux_list_name.append(splitted[j])
                    aux_list_name.append(" ")
                else:
                    k = j
                    break

            for text in range(len(aux_list_name)-1):
                aux = aux + aux_list_name[text]

            aux_list.append(aux)
            aux_list_name = []
            aux = ''

            aux_list.append(teste.split(" ")[j])

            #TURMA
            for r in range(j+1, len(splitted)):
                aux_list_name.append(splitted[r])
                aux_list_name.append(" ")

            for text in range(len(aux_list_name)-1):
                aux = aux + aux_list_name[text]

            aux_list.append(aux)
            aux_list.append(premiacao)

            print(aux_list)

            aux_list_name = []

            medalhas.append(aux_list)

            aux_list = []
            aux = ''

            print("\n")

    except:
        break

print(medalhas)
save.salvar(medalhas)