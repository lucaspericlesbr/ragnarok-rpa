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

def rotate_screen():

    while keyboard.is_pressed('q') == False:
        coords = locateCenterOnScreen('mushroom_landmark.png', confidence=0.85)

        if coords != None:
            moveTo(coords.x-400, coords.y+250)
            drag(92, 0, 2, button='right')
            break

        else:
            continue

def walking_to_the_castle():
    
    coords = locateCenterOnScreen('weight_landmark.png', confidence=0.85)

    while keyboard.is_pressed('q') == False:
        landmark = locateCenterOnScreen('recepcionist_landmark.png', confidence=0.80)    

        if landmark != None:
            break
        
        else:
            moveTo(coords.x+850, coords.y-50)
            click(coords.x+850, coords.y-50)
    time.sleep(2)

def second_npc():

    while keyboard.is_pressed('q') == False:
        recepcionist = locateCenterOnScreen('recepcionist_landmark.png', confidence=0.70)

        if recepcionist != None:
            moveTo(recepcionist)
            click(recepcionist.x, recepcionist.y)
            break

        else:
            continue

    for i in range(0, 6):
        press('enter')
        time.sleep(0.5)

def third_npc():
    time.sleep(2)

    landmark = locateCenterOnScreen('second_room_landmark.png', confidence=0.85)
    moveTo(landmark.x+380, landmark.y-290)
    click(landmark.x+380, landmark.y-290)

    while keyboard.is_pressed('q') == False:
        instrutor = locateCenterOnScreen('battle_instructor.png', confidence=0.60)

        if instrutor != None:
            break
            
        else:
            moveTo(landmark.x+335, landmark.y-290)
            click(landmark.x+335, landmark.y-290)
    time.sleep(2)

    while keyboard.is_pressed('q') == False:
        instrutor = locateCenterOnScreen('battle_instructor.png', confidence=0.70)

        if instrutor != None:
            moveTo(instrutor)
            click(instrutor.x, instrutor.y)
            break

        else:
            continue
    
    for i in range(0, 12):
        press('enter')
        time.sleep(0.5)

    moveTo(instrutor)
    click(instrutor.x, instrutor.y)

    for k in range(0, 3):
        press('enter')
        time.sleep(0.5)

def fourth_npc():

    while keyboard.is_pressed('q') == False:
        instrutor = locateCenterOnScreen('skill_instructor.png', confidence=0.70)

        if instrutor != None:
            moveTo(instrutor)
            click(instrutor.x, instrutor.y)
            break

        else:
            continue

    for i in range(0, 16):
        press('enter')
        time.sleep(0.5)

def fifth_npc():

    while keyboard.is_pressed('q') == False:
        instrutor = locateCenterOnScreen('skill_instructor.png', confidence=0.70)

        if instrutor != None:
            moveTo(instrutor.x+490, instrutor.y+50)
            click(instrutor.x+490, instrutor.y+50)
            break

        else:
            continue
    time.sleep(2)

    while keyboard.is_pressed('q') == False:
        instrutor = locateCenterOnScreen('third_npc_landmark.png', confidence=0.70)

        if instrutor != None:
            moveTo(instrutor)
            click(instrutor.x, instrutor.y)
            break
            
        else:
            continue
    
    for i in range(0, 3):
        press('enter')
        time.sleep(0.5)

def sixth_npc():

    while keyboard.is_pressed('q') == False:
        instrutora = locateCenterOnScreen('item_instructor.png', confidence=0.70)

        if instrutora != None:
            moveTo(instrutora)
            click(instrutora.x, instrutora.y)
            break
            
        else:
            continue
    
    for i in range(0, 15):
        press('enter')
        time.sleep(0.5)

    moveTo(instrutora)
    click(instrutora.x, instrutora.y)
    
    for k in range(0, 5):
        press('enter')
        time.sleep(0.5)

def seventh_npc():

    while keyboard.is_pressed('q') == False:
        instrutor = locateCenterOnScreen('battle_instructor[2].png', confidence=0.70)

        if instrutor != None:
            moveTo(instrutor)
            click(instrutor.x, instrutor.y)
            break
            
        else:
            continue

    for i in range(0, 13):
        press('enter')
        time.sleep(0.5)
    
    for k in range(0, 3):
        press('down')

    for j in range(0, 2):
        press('enter')
        time.sleep(0.5)

def eighth_npc():

    while keyboard.is_pressed('q') == False:
        helper = locateCenterOnScreen('helper.png', confidence=0.70)

        if helper != None:
            moveTo(helper)
            click(helper.x, helper.y)
            break
            
        else:
            continue
        
    for i in range(0, 6):
        press('enter')
        time.sleep(0.5)

def novice_field():

    for i in range(0, 2):
        click(1515,70)
        time.sleep(2)

    while keyboard.is_pressed('q') == False:
        funcionario = locateCenterOnScreen('checking_officer.png', confidence=0.8)
        screen = locateCenterOnScreen('screeen_checking_officer.png')

        if locateOnScreen('dead_popup.png', confidence=0.95):
            time.sleep(0.2)
            mouseUp()
            click(1300,725)
            time.sleep(0.5)
            click(1365,605)
            time.sleep(0.5)
            novice_field()

        if funcionario != None:
            time.sleep(0.2)
            mouseUp()
            click(funcionario.x, funcionario.y)

            if screen != None:
                break

        else:
            moveTo(1290,80)
            time.sleep(0.2)
            mouseDown()
    
    for k in range(0, 3):
        press('enter')
        time.sleep(0.3)
    time.sleep(2)

def novice_instructor():

    mouseUp()
    time.sleep(1)

    while keyboard.is_pressed('q') == False:
        landmark = locateCenterOnScreen('pillar.png', confidence=0.80)

        if landmark != None:
            moveTo(landmark.x+100, landmark.y-50)
            click(landmark.x+100, landmark.y-50)
            break
            
        else:
            continue
    time.sleep(2)

    while keyboard.is_pressed('q') == False:
        instrutor = locateCenterOnScreen('novice_instructor.png', confidence=0.60)

        if instrutor != None:
            moveTo(instrutor)
            click(instrutor.x, instrutor.y)
            break
            
        else:
            continue

    for i in range(0, 12):
        press('enter')
        time.sleep(0.5)

    for k in range(0, 6):
        press('down')    

    for j in range(0, 2):
        press('enter')
        time.sleep(0.5)

def final_instructor():
    
    while keyboard.is_pressed('q') == False:
        instrutor = locateCenterOnScreen('final_instructor.png', confidence=0.80)

        if instrutor != None:
            moveTo(instrutor)
            click(instrutor.x, instrutor.y)
            break
            
        else:
            continue
    
    # MARCANDO OPÇÕES
    for i in range(0, 12):
        press('enter')
        time.sleep(0.5)

    press('down')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('down')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('down')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)

    for k in range(0, 18):
        press('enter')
        time.sleep(0.5)

    press('down')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('down')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('down')
    time.sleep(0.5)
    press('down')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('down')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('down')
    time.sleep(0.5)
    press('down')
    time.sleep(0.5)

    for p in range(0, 6):
        press('enter')
        time.sleep(0.5)

    press('down')
    time.sleep(0.5)

    for h in range(0, 17):
        press('enter')
        time.sleep(0.5)

def skillpoint():

    while keyboard.is_pressed('q') == False:
        skill = locateCenterOnScreen('skillpoint.png')

        if skill != None:
            moveTo(skill)
            break                
            
        else:
            keyDown('alt')
            time.sleep(0.5)
            press('s')
            keyUp('alt')

    for i in range(0, 6):
        click(skill.x, skill.y)
        time.sleep(0.2)

    while keyboard.is_pressed('q') == False:
        apply = locateCenterOnScreen('apply_skill.png')

        if apply != None:
            moveTo(apply)
            click(apply.x, apply.y)
            break                
            
        else:
            continue
        
    while keyboard.is_pressed('q') == False:
        ok = locateCenterOnScreen('ok_button.png')

        if ok != None:
            moveTo(ok)
            click(ok.x, ok.y)
            break                
            
        else:
            continue
        
    keyDown('alt')
    time.sleep(0.5)
    press('s')
    keyUp('alt')

def teleport():
    # ACHAR E CLICAR NA ABA DE ITEMS C
    while keyboard.is_pressed('q') == False:
        landmark_C = locateCenterOnScreen('landmark_inventory_C.png', confidence=0.90)

        if landmark_C != None:
            moveTo(landmark_C)
            DoubleClick(landmark_C.x, landmark_C.y)
            break                
            
        else:
            keyDown('alt')
            time.sleep(0.5)
            press('e')
            keyUp('alt')
            time.sleep(0.5)

    # ACHAR E CLICAR NA ASALA DE BORBOLETA
    while keyboard.is_pressed('q') == False:
        wing = locateCenterOnScreen('butterfly_wing.png')

        if wing != None:
            moveTo(wing)
            DoubleClick(wing.x, wing.y)
            break                
            
        else:
            keyDown('alt')
            time.sleep(0.5)
            press('e')
            keyUp('alt')
            time.sleep(0.5)

    keyDown('alt')
    time.sleep(0.5)
    press('e')
    keyUp('alt')

def last_kafra():

    while keyboard.is_pressed('q') == False:
        kafra = locateCenterOnScreen('last_kafra.png', confidence=0.80)

        if kafra != None:
            moveTo(kafra)
            click(kafra.x, kafra.y)
            break                
            
        else:
            continue

    time.sleep(1)
    press('enter')
    time.sleep(0.5)
    press('down')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)

def pass_itens():

    while keyboard.is_pressed('q') == False:
        landmark_C = locateCenterOnScreen('landmark_inventory_C.png', confidence=0.90)

        if landmark_C != None:
            moveTo(landmark_C)
            DoubleClick(landmark_C.x, landmark_C.y)
            break                
            
        else:
            keyDown('alt')
            time.sleep(0.5)
            press('e')
            keyUp('alt')
            time.sleep(0.5)

    while keyboard.is_pressed('q') == False:
        all_C = locateCenterOnScreen('all_items_C.png', confidence=0.80)

        if all_C != None:
            moveTo(all_C.x-80, all_C.y)
            break                
            
        else:
            keyDown('alt')
            time.sleep(0.5)
            press('e')
            keyUp('alt')
            time.sleep(0.5)

    keyDown('alt')
    for i in range(0, 6):
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(0.5)
    keyUp('alt')

    while keyboard.is_pressed('q') == False:
        landmark_I = locateCenterOnScreen('landmark_inventory_I.png', confidence=0.90)

        if landmark_I != None:
            moveTo(landmark_I)
            DoubleClick(landmark_I.x, landmark_I.y)
            break                
            
        else:
            keyDown('alt')
            time.sleep(0.5)
            press('e')
            keyUp('alt')
            time.sleep(0.5)

    while keyboard.is_pressed('q') == False:
        all_I = locateCenterOnScreen('all_items_I.png', confidence=0.80)

        if all_I != None:
            moveTo(all_C.x-20, all_C.y)
            break                
            
        else:
            keyDown('alt')
            time.sleep(0.5)
            press('e')
            keyUp('alt')
            time.sleep(0.5)

    keyDown('alt')
    for i in range(0, 1):
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(0.5)
    keyUp('alt')

def logout():

    while keyboard.is_pressed('q') == False:
        config = locateCenterOnScreen('screen_configuration.png', confidence=0.90)

        if config != None:
            break                
            
        else:
            press('esc')

    while keyboard.is_pressed('q') == False:
        logout = locateCenterOnScreen('character_select.png',)

        if logout != None:
            moveTo(logout)
            click(logout.x, logout.y)
            break                
            
        else:
            press('esc')

def delete_character():

    # EXCLUIR PERSONAGEM
    while keyboard.is_pressed('q') == False:
        delete = locateCenterOnScreen('delete_character.png', confidence=0.80)

        if delete != None:
            moveTo(delete)
            click(delete.x, delete.y)
            break                
            
        else:
            continue

    # EXCLUIR
    while keyboard.is_pressed('q') == False:
        exclusion = locateCenterOnScreen('delete_option.png', confidence=0.70)

        if exclusion != None:
            moveTo(exclusion)
            click(exclusion.x, exclusion.y)
            break                
            
        else:
            continue

    # OK
    while keyboard.is_pressed('q') == False:
        ok = locateCenterOnScreen('ok_button.png', confidence=0.80)

        if ok != None:
            moveTo(ok)
            click(ok.x, ok.y)
            break                
            
        else:
            continue

    keyDown('ctrl')
    time.sleep(1)
    press('v')
    time.sleep(1)
    keyUp('ctrl')

    time.sleep(1)
    press('enter')
    