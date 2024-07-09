import pyautogui
import pyperclip
import time


class MeuRobo():
    
   def __init__(self, tempo_espera):
       self.tempo_espera = tempo_espera
       pyautogui.PAUSE = 1

    
   def abrir_programa(self, nome_programa):
       pyautogui.press("win")
       pyautogui.write(nome_programa)
       pyautogui.press("enter")

       if nome_programa.lower() in 'chrome':
           #entrando no chrome tem que entrar no seu chrome, login
           # aguardar
           time.sleep(3)
           pyautogui.click(x=516, y=446)

   
   def entrar_site(self, site):
        #time.sleep(2)
        # entrando no site 
        # pyperclip.copy(site)
        # pyautogui.hotkey("ctrl", "v")
        # pyautogui.press("enter")
        #aguardar um pouco
        self.escrever_e_enter(site)
        self.aguardar()

   def escrever_e_enter(self, texto):
        pyperclip.copy(texto)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
       
   def aguardar(self):
       time.sleep(self.tempo_espera)

    
   def pesquisar_no_campo(self, texto):
       self.escrever_e_enter(texto)
       self.aguardar()    
    
   #botao padrao = left
   def clicar(self, xa, ya, botao = 'left'):
       #botao = right ou left
       # clicando no campo que desejo
       pyautogui.click(x= xa, y=ya, button = botao)

   def pegar_posicao(self):
        n_tempo=5
        
        for i in range(n_tempo):
            print(f'pegando posição em {n_tempo-i} segundos')
            time.sleep(1)
        print(pyautogui.position())       

   def extrair_link(self, x, y):
       self.clicar(x,y, botao='right')
       pyautogui.press("up")
       pyautogui.press("up")
       pyautogui.press("enter")  
       # printar o texto copiado
       texto_2 = pyperclip.paste()        
       print(texto_2)
       self.texto_final = texto_2


   def abrir_nova_aba(self, x, y): 
       self.clicar(x,y, botao='right')
       pyautogui.press("down")
       pyautogui.press("enter")  


   def rolar_pagina(self, posicao):

        if posicao in 'desce':
            pyautogui.scroll(-2)  # scroll down 10 "clicks" desce

        elif posicao in 'sobe':
            pyautogui.scroll(2)   # scroll up 10 "clicks" sobe
            
        #pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"


   def salvar_imagem(self, x, y):
       pyautogui.alert('Salve seu arquivo no seu computador, na pasta que você deseja!')
       self.clicar(x,y, botao='right')
       # aguardar
       self.aguardar()
       pyautogui.press("down")
       pyautogui.press("down")       
       pyautogui.press("enter")       
    
   def alertaInicial_computador(self):
       pyautogui.alert('O código vai começar. Não mexa em NADA enquanto o código tiver rodando. Quando finalizar, eu te aviso')
       self.aguardar()


   def alertaFinal_computador(self):
       pyautogui.alert('O código terminou, pode pegar seu notebook de volta!')
       self.aguardar()
