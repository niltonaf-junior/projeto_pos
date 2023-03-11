from time import sleep
import pyautogui

pyautogui.PAUSE=1


def move(locate):
    x,y = pyautogui.center(locate)
    pyautogui.moveTo(x,y,duration=1)

def move_click(locate):
    move(locate)
    pyautogui.click()    

sleep(3)
verificar_tela = pyautogui.locateOnScreen('images/nota_compras.png',confidence=0.8)
if verificar_tela == None:
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('g')
    sleep(1)
    pyautogui.write('nota de compra')
    sleep(1)
    pyautogui.press('enter') 

with open ('dados.txt','r') as file:
    for linha in file:
        dados = linha.split(',') 
        cod_empresa = dados[0]
        nro_nota = dados[1]
        data_emissao = dados[2]
        data_vencimento = dados[3]
        cod_parceiro = dados[4]
        tipo_negociacao = dados[5]
        primeiro_aprovador = dados[6]
        segundo_aprovador = dados[7]
        observacao = dados[8]
        cod_produto = dados[9]
        quantidade = dados[10]
        valor = dados[11]
        projeto = dados[12]
        centro_resultado = dados[13]
        natureza = dados[14]
  

    empresa = pyautogui.locateOnScreen('images/empresa.png',confidence=0.8)
    while empresa == None:
        sleep(0.5)
        empresa = pyautogui.locateOnScreen('images/empresa.png',confidence=0.8)

    move_click(empresa)

    #preencher campo empresa
    pyautogui.write(cod_empresa)
    pyautogui.press('tab')
    #prencher nunota
    pyautogui.write(nro_nota)
    pyautogui.press('tab')
    #preencher serie
    pyautogui.write('0')
    pyautogui.press('tab')
    pyautogui.write(data_emissao)
    pyautogui.press('tab')
    pyautogui.write(data_vencimento)
    pyautogui.press('tab',presses=5)
    pyautogui.write(cod_parceiro)
    pyautogui.press('tab',presses=2)
    pyautogui.write(tipo_negociacao)
    pyautogui.press('tab')
    pyautogui.write(primeiro_aprovador)
    pyautogui.press('tab')
    pyautogui.write(segundo_aprovador)
    pyautogui.press('tab')
    pyautogui.write(observacao)
    pyautogui.scroll(300)
    sleep(1)
    pyautogui.press('f7')
    nrounico = pyautogui.locateOnScreen('images/nro_unicovazio.png',confidence=0.8)
    while nrounico == None:
        sleep(0.5)
        nrounico = pyautogui.locateOnScreen('images/nro_unicovazio.png',confidence=0.8)
    sleep(2)
    pyautogui.write(cod_produto)
    pyautogui.press('tab')
    sleep(1.5)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('1')
    pyautogui.press('tab')
    pyautogui.write(valor)
    pyautogui.press('tab',presses=2)
    pyautogui.write(projeto)
    pyautogui.press('tab')
    pyautogui.write(centro_resultado)
    pyautogui.press('tab')
    pyautogui.write(natureza)
    pyautogui.press('tab')
    pyautogui.press('f7')

    local = pyautogui.locateOnScreen('images/local.png',confidence=0.8)
    while local == None:
        sleep(0.5)
        local = pyautogui.locateOnScreen('images/local.png',confidence=0.8)

    opcoes = pyautogui.locateOnScreen('images/opcoes.png',confidence=0.8)
    move_click(opcoes)
    sleep(0.7)
    anexo = pyautogui.locateOnScreen('images/anexo.png',confidence=0.8)
    move_click(anexo)
    incluir = pyautogui.locateOnScreen('images/incluir.png',confidence=0.8)
    move_click(incluir)
    verificar_anexo = pyautogui.locateOnScreen('images/verificar_anexo.png',confidence=0.8)
    while verificar_anexo == None:
        sleep(0.7)
        verificar_anexo = pyautogui.locateOnScreen('images/verificar_anexo.png',confidence=0.8)

    pyautogui.press('tab')
    pyautogui.write('nf')
    pyautogui.press('tab')
    sleep(0.5)
    pyautogui.press('enter')
    abrir = pyautogui.locateOnScreen('images/abrir.png',confidence=0.8)
    while abrir == None:
        sleep(0.7)
        abrir = pyautogui.locateOnScreen('images/abrir.png',confidence=0.8)
    sleep(1)
    pyautogui.write(nro_nota)
    pyautogui.press('down')
    sleep(0.5)
    pyautogui.press('enter') 
    salvar_anexo = pyautogui.locateOnScreen('images/salvar_anexo.png',confidence=0.8)
    move_click(salvar_anexo)   
    sleep(0.7)
    ok = pyautogui.locateOnScreen('images/ok.png',confidence=0.8)
    move_click(ok)
    confirmar = pyautogui.locateOnScreen('images/confirmar.png',confidence=0.8)
    move_click(confirmar)
    liberacao = pyautogui.locateOnScreen('images/liberacao.png',confidence=0.8)
    while liberacao == None:
        liberacao = pyautogui.locateOnScreen('images/liberacao.png.png',confidence=0.8)
        sleep(1)

    sleep(1)
    pyautogui.write(primeiro_aprovador)
    definir_liberador = pyautogui.locateOnScreen('images/definir_liberador.png',confidence=0.8)
    move_click(definir_liberador)
    sleep(0.5)
    pyautogui.press('esc')