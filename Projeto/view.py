from controller import *
import os
import sys

#def main():
### MENU ###

lista_jogadores = []

while True: 
    print("""
=-==-==-==-==-==-==-==-==-==-==-
|                              |
|        "N" em Linha \U0001f579\uFE0F        |
|                              |
|    [IJ] - Iniciar Jogo       |
|    [RJ] - Registar Jogador   |
|    [EJ] - Eliminar Jogador   |
|    [LJ] - Listar Jogador     |
|    [SM] - Sair do Menu       |
|                              |
=-==-==-==-==-==-==-==-==-==-==-
""")
    
    opcao_menu = input("Introduza a sua opção: ").lower()
   
    if opcao_menu == "ij":
        print("1")

    elif opcao_menu == "rj":
        nome_registar = input("Introduza o nome a registar: ").lower()
        while nome_registar in lista_jogadores:
            print("Jogador existente.")
            nome_registar= input("Introduza o nome a registar: ").lower()
        registar_jogador(nome_registar, lista_jogadores)
        print("Jogador registado com  sucesso.")

        #ver ficheiros e armazenar os nomes dentro dos ficheiros
            
    elif opcao_menu == "ej":
        if len(lista_jogadores) == 0:
            print("Não existem jogadores registados")
        else:
            nome_remover = input("Introduza o nome a remover: ").lower()
            while nome_remover not in lista_jogadores:
                print("Jogador não existente.")
                nome_remover = input("Introduza o nome a eliminar: ").lower()
            remover_jogador(nome_remover, lista_jogadores)
            print("Jogador removido com sucesso.")
            

    elif opcao_menu == "lj":
        pass

    elif opcao_menu == "sm":
        break
    
    else:
        print("Opção inválida.")

        