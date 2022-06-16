from pyautogui import *
import time
import keyboard
import random
import win32api, win32con

time.sleep(5)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def create_char():

    while keyboard.is_pressed('q') == False:

        coords = locateCenterOnScreen('empty_field.png')
        text_box = locateCenterOnScreen('name_field.png', confidence=0.80)
        create_char = locateCenterOnScreen('create.png')    

        if coords != None:
            moveTo(coords)
            click(coords.x, coords.y)
            time.sleep(1)
        
        elif text_box != None:
            write('The Novice')
            time.sleep(1)

        elif create_char != None:
            moveTo(create_char)
            click(create_char.x, create_char.y)
            time.sleep(1)
            press('enter')
            break

        else:
            continue

def close_daily_reward():

    time.sleep(3)
    coords = locateCenterOnScreen('close_daily_reward.png') 

    if coords != None:
        moveTo(coords)
        click(coords.x, coords.y)

def initial_kafra():

    while keyboard.is_pressed('q') == False:
        coords = locateCenterOnScreen('initial_kafra.png', confidence=0.65)

        if coords != None:
            moveTo(coords)
            click(coords.x, coords.y)
            break
        
        else:
            continue
            
    for i in range(0, 12):
        press('enter')
        time.sleep(0.5)

    while keyboard.is_pressed('q') == False:
        coords = locateCenterOnScreen('initial_kafra.png', confidence=0.65)

        if coords != None:
            moveTo(coords)
            click(coords.x, coords.y)
            break

        else:
            continue

    for K in range(0, 4):
        press('enter')
        time.sleep(0.5)

# def rotate_screen():

#     while keyboard.is_pressed('q') == False:
#         coords = locateCenterOnScreen('mushroom.png', confidence=0.85)

#         if coords != None:
#             print('ACHOU O "COGUMELO" PONTO DE REFERENCIA')
#             moveTo(coords.x-400, coords.y+250)
#             drag(92, 0, 2, button='right')
#             time.sleep(2)
#             break

#         else:
#             print('NÃO ACHOU O PONTO DE REFERENCIA')

# def walking_to_the_castle():
#     coords = locateCenterOnScreen('board_state.png', confidence=0.85)

#     while keyboard.is_pressed('q') == False:
#         landmark = locateCenterOnScreen('landmark_recepcionista.png', confidence=0.80)

#         if landmark != None:
#             print('ACHOU O PONTO DE PARADA E PAROU')
#             break
        
#         else:
#             print('ANDANDO ATÉ ENCONTRAR PONTO DE PARADA')
#             moveTo(coords.x+150, coords.y)
#             click(coords.x+150, coords.y)

# def second_npc():
#     click(1105,100)
#     time.sleep(4)

#     if locateOnScreen('recepcionista.png') != None:
#         click(1490,200)
#     else:
#         click(1490,200)

#     for i in range(0, 6):
#         press('enter')
#         time.sleep(0.5)

# def third_npc():
#     click(1068,72)
#     time.sleep(3)
#     click(1330,100)
#     time.sleep(5)

#     if locateOnScreen('instrutor_de_batalha.png') != None:
#         click(1435,235)
#         time.sleep(1)
    
#     else:
#         click(1435,235)
#         time.sleep(1)

#     for i in range(0, 12):
#         press('enter')
#         time.sleep(0.5)

#     click(1435,235)

#     for k in range(0, 3):
#         press('enter')
#         time.sleep(0.5)

# def fourth_npc():
#     if locateOnScreen('instrutor_de_habilidade.png') != None:
#         click(1245,350)
#         time.sleep(1)
#     else:
#         click(1245,350)
#         time.sleep(1)
        

#     for i in range(0, 16):
#         press('enter')
#         time.sleep(0.5)

# def walking_fifth_npc():
#     time.sleep(1)
#     click(2100,560)
#     time.sleep(3)
#     click(2100,560)
#     time.sleep(3)

# def fifth_npc():
#     if locateOnScreen('instrutora_de_itens.png') != None:
#         click(1250,350)
#         time.sleep(1)
#     else:
#         click(1245,350)
#         time.sleep(1)

#     for i in range(0, 15):
#         press('enter')
#         time.sleep(0.5)

#     click(1245,350)
#     time.sleep(1)

#     for k in range(0, 5):
#         press('enter')
#         time.sleep(0.5)

# def sixth_npc():
#     if locateOnScreen('instrutor_de_batalha_02.png') != None:
#         click(750,360)
#         time.sleep(1)
#     else:
#         click(750,360)
#         time.sleep(1)

#     for i in range(0, 13):
#         press('enter')
#         time.sleep(0.5)

#     for k in range(0, 3):
#         press('down')
        
#     press('enter')
#     time.sleep(0.5)
#     press('enter')
#     time.sleep(0.5)

# def seventh_npc():
#     if locateOnScreen('ajudante.png') != None:
#         click(1780,365)
#         time.sleep(1)
#     else:
#         click(1780,365)
#         time.sleep(1)

#     for i in range(0, 6):
#         press('enter')
#         time.sleep(0.5)  

# def novice_field():

#     for i in range(0, 2):
#         click(1515,70)
#         time.sleep(2)

#     while True:

#         if locateOnScreen('dead_popup.png', confidence=0.95):
#             click(1300,725)
#             time.sleep(1)
#             click(1365,605)
#             time.sleep(1)
#             novice_field()


#         posi_check = locateOnScreen('funcionario_de_checagem.png', confidence=0.8)

#         if posi_check != None:
#             print('achou')
#             func_checagem = center(posi_check)
#             #time.sleep(1.5)
#             click(func_checagem.x, func_checagem.y)
#             #time.sleep(1)

#             for k in range(0, 3):
#                 press('enter')
#                 time.sleep(0.2)
#                 print('terminou de falar')
#                 break
        
#         elif locateOnScreen('pilar.png', confidence=0.95) != None:
#             print('achou o pilar')
#             break

#         else:
#             print('Nao achou')
#             click(1290,80)

# def instrutor_de_aprendizes():

#     time.sleep(5)

#     click(905,300)
#     time.sleep(2)
#     click(1290,350)

#     for i in range(0, 12):
#         press('enter')
#         time.sleep(0.5)
    
#     for k in range(0, 6):
#         press('down')
    
#     press('enter')
#     time.sleep(0.5)
#     press('enter')
#     time.sleep(0.5)

# def instrutor_final():
#     time.sleep(2)
#     click(1710,100)

#     for i in range(0, 67):
#         press('enter')
#         time.sleep(0.5)

# def get_out():
#     time.sleep(2)
#     click(1740,900)
#     time.sleep(2)
#     click(1500,810)
#     time.sleep(2)
#     click(1950,550)
#     time.sleep(2.5)
#     click(1900,560)
#     time.sleep(2.5)
#     click(1900,560)
#     time.sleep(2.5)
#     click(1900,560)
#     time.sleep(2)
#     click(1795,560)
#     time.sleep(2)
#     click(1290,1030)
#     time.sleep(2)
#     click(1705,680)

# def skillpoint():
#     time.sleep(2)
#     keyDown('alt')
#     time.sleep(1)
#     press('s')

#     for i in range(0, 6):
#         moveTo(768,257)
#         mouseDown(); mouseUp()  

#     keyUp('alt')
#     time.sleep(1)
#     click(1160,590)
#     time.sleep(1)
#     click(1363,605)

#     time.sleep(1)
#     click(1230,216)

# def last_kafra():
#     time.sleep(1)
#     click(1700,470)
#     time.sleep(0.5)
#     press('enter')
#     time.sleep(0.5)
#     press('down')
#     time.sleep(0.5)
#     press('enter')
#     time.sleep(0.5)
#     press('enter')

# def pass_itens():

#     time.sleep(2)
#     keyDown('alt')
#     time.sleep(1)
#     press('e')
#     time.sleep(1)
#     keyUp('alt')

#     time.sleep(1)
#     moveTo(1427,516)
#     click(1427,516)

#     time.sleep(1)
#     moveTo(1503,520)

#     keyDown('alt')

#     for i in range(0, 6):
#         win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
#         time.sleep(0.2)
#         win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
#         time.sleep(0.5)
#     keyUp('alt')

#     time.sleep(1)
#     click(1425,560)

#     time.sleep(1)
#     moveTo(1535,520)
#     time.sleep(0.5)
#     keyDown('alt')
#     time.sleep(1)
#     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
#     time.sleep(0.2)
#     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
#     time.sleep(0.5)
#     keyUp('alt')
#     time.sleep(1)
#     keyDown('alt')
#     press('e')
#     keyUp('alt')

#     time.sleep(1)
#     click(1311,942)

# def deslogar():

#     while True:
#         press('esc')
#         time.sleep(1)

#         if locateOnScreen('janela_de_configuracoes.png', confidence=0.95) != None:
#             click(1300,725)
#             break

# def delete_character():
#     time.sleep(3)

#     #if locateOnScreen('delete_character.png', confidence=0.95) != None:
#     click(1670,510)

#     time.sleep(2)

#     #if locateOnScreen('delete_option.png', confidence=0.95) != None:
#     click(1670,535)
#     time.sleep(2)
#     click(1360,605)

#     keyDown('ctrl')
#     time.sleep(1)
#     press('v')
#     time.sleep(1)
#     keyUp('ctrl')
#     click(1395,530)
    

            
# while True:
#     create_char()
#     time.sleep(2)
#     close_window_daily()
#     kafra_initial()
#     time.sleep(2)
#     rotate_screen()
#     walking_to_the_castle()
#     time.sleep(2)
#     second_npc()
#     time.sleep(2)
#     third_npc()
#     time.sleep(2)
#     fourth_npc()
#     time.sleep(2)
#     walking_fifth_npc()
#     time.sleep(2)
#     fifth_npc()
#     time.sleep(2)
#     sixth_npc()
#     time.sleep(2)
#     seventh_npc()
#     time.sleep(2)
#     novice_field()
#     time.sleep(2)
#     instrutor_de_aprendizes()
#     time.sleep(2)
#     instrutor_final()
#     time.sleep(2)
#     get_out()
#     time.sleep(2)
#     skillpoint()
#     time.sleep(2)
#     last_kafra()
#     time.sleep(2)
#     pass_itens()
#     time.sleep(2)
#     deslogar()
#     time.sleep(2)
#     delete_character()
#     time;sleep(5)