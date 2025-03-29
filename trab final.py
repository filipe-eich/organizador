"""
Programa: Trab_final
Descrição: Este programa refere-se ao trab. final da disciplina e organiza arquivos como documentos e planilhas em pastas
Autor: Luis Filipe Eich
Data: 28/03/2025
Versao: 0.0.1
"""


#Bibliotecas

import os
import shutil


#Alocaçao de memoria

PASTA_PLANILHAS = ""
PASTA_DOCUMENTOS = ""


#Entrada de dados

PASTA_PLANILHAS = 'planilhas'
PASTA_DOCUMENTOS = 'documentos'


# Processamento de dados

os.makedirs(PASTA_PLANILHAS, exist_ok=True)

os.makedirs(PASTA_DOCUMENTOS, exist_ok=True)



for arquivo in os.listdir():
    if os.path.isfile(arquivo):
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        
        if extensao == '.xls':
            shutil.move(arquivo, os.path.join(PASTA_PLANILHAS, arquivo))
        elif extensao in ('.doc', '.docx'):
            shutil.move(arquivo, os.path.join(PASTA_DOCUMENTOS, arquivo))




#Saida de dados

print("**Olá!! As alterações foram concluídas!**\nArquivos organizados nas pastas 'planilhas' e 'documentos'.")



