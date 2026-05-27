# Imports
from utils.console import (
    start_text,
    main_menu,
    choose_keys_menu,
    start_count_text,
    register_movement,
    register_left_clicker_begin,
    register_left_clicker_end,
    register_fishing,
    register_sword,
    exit_text
)
from pynput.keyboard import Controller, Key, Listener
from pynput.mouse import Controller as MouseController, Button
from utils.keys import KeysChoice, WASD_KEYS, ARROW_KEYS
import threading

# Variáveis globais
keyboard = Controller()
mouse = MouseController()
stop_event = threading.Event()
keys_choice = KeysChoice.WASD

# Funções
def move_character_thread() -> None:
    keys = WASD_KEYS if keys_choice == KeysChoice.WASD else ARROW_KEYS
    while not stop_event.is_set():
        for key in keys:
            if stop_event.is_set():
                break
            
            keyboard.press(key)
            register_movement(key)
            
            # Espera 0.5s OU até o evento de parada ser acionado
            if stop_event.wait(0.5):
                keyboard.release(key)
                break
            
            keyboard.release(key)
            
            # Espera 5s OU até o evento de parada ser acionado
            if stop_event.wait(5):
                break

def left_click_mouse_thread() -> None:
    mouse.press(Button.left)
    register_left_clicker_begin()
    stop_event.wait() # Trava a thread eficientemente até o stop_event ser acionado
    mouse.release(Button.left)
    register_left_clicker_end()

def fishing_on_minecraft_thread() -> None:
    while not stop_event.is_set():

        # Lança a isca
        mouse.press(Button.right)
        stop_event.wait(0.1) # Segura o botão por 100ms
        mouse.release(Button.right)
        register_fishing()
        
        # Espera 15 segundos ou até a parada ser acionada
        if stop_event.wait(15):
            break

def skeleton_farm_on_minecraft_thread() -> None:
    while not stop_event.is_set():

        # Dá o golpe de espada
        mouse.press(Button.left)
        stop_event.wait(0.1) # Segura o botão por 100ms
        mouse.release(Button.left)
        register_sword()
        
        # Espera 3 segundos ou até a parada ser acionada
        if stop_event.wait(3):
            break

def on_press(key: Key) -> None:
    if key == Key.space:
        stop_event.set()
        return False

if __name__ == '__main__':
    start_text()
    while True:
        option = main_menu()
        match option:
            
            # Mudança do sistema de movimento
            case 1:
                keys_choice = KeysChoice(choose_keys_menu())
            
            # Iniciar a movimentação
            case 2:
                print('\nIniciando a movimentação em breve...\n')
                start_count_text()
                stop_event.clear()
                movement_thread = threading.Thread(target=move_character_thread)
                movement_thread.start()
                with Listener(on_press=on_press) as listener:
                    listener.join()
                movement_thread.join()
            
            # Iniciar a tecla esquerda do mouse
            case 3:
                print('\nIniciando o botão esquerdo do mouse em breve...\n')
                start_count_text()
                stop_event.clear()
                mouse_thread = threading.Thread(target=left_click_mouse_thread)
                mouse_thread.start()
                with Listener(on_press=on_press) as listener:
                    listener.join()
                mouse_thread.join()

            # Iniciar a pescaria no Minecraft
            case 4:
                print('\nIniciando a pescaria no Minecraft em breve...\n')
                start_count_text()
                stop_event.clear()
                fishing_thread = threading.Thread(target=fishing_on_minecraft_thread)
                fishing_thread.start()
                with Listener(on_press=on_press) as listener:
                    listener.join()
                fishing_thread.join()

            # Iniciar a farm de esqueleto no Minecraft
            case 5:
                print('\nIniciando a farm de esqueleto no Minecraft em breve...\n')
                start_count_text()
                stop_event.clear()
                skeleton_thread = threading.Thread(target=skeleton_farm_on_minecraft_thread)
                skeleton_thread.start()
                with Listener(on_press=on_press) as listener:
                    listener.join()
                skeleton_thread.join()

            # Finalizar o programa
            case 6:
                break
    
    exit_text()
