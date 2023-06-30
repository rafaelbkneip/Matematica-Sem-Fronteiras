#Módulo para salvar lista em um arquivo xlsx / Module to save the list to an xlsx file

#Importações / Imports
import xlsxwriter

#Função para salvar o arquivo / Function to save thee file
def salvar(unica):

    #Escrever o arquivo / Write the file
    workbook = xlsxwriter.Workbook('Medalhas.xlsx')
    #Adicionar uma aba / Add a sheet
    sheet = workbook.add_worksheet()   

    try:
        #Cada elemento da lista tornará-se uma linha do documento / Each list element will be a row in the file
        for i in range(len(unica)):
            #O número de colunas é definido com base no tamanho de cada elemento da lista / The column number is defined by the length of each list element
            for j in range(len(unica[0])):
                sheet.write(i+1, j, unica[i][j])

    except Exception as e:
        print(e)

    #Fechar o arquivo / Close the file
    workbook.close()

    return print("Finalizado!")