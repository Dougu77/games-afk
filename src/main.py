# Imports
from utils.console import start_text, main_menu, choose_keys_menu, start_program_text, register_movement, exit_text
from pynput.keyboard import Controller, Key, Listener
from utils.keys import KeysChoice, WASD_KEYS, ARROW_KEYS
import threading

# Variáveis globais
keyboard = Controller()
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

def on_press(key: Key) -> None:
    if key == Key.space:
        stop_event.set()
        return False

if __name__ == '__main__':
    start_text()
    while True:
        option = main_menu()
        match option:
            
            # Mudança do sistema de teclas
            case 1:
                keys_choice = KeysChoice(choose_keys_menu())
            
            # Iniciar o programa
            case 2:
                start_program_text()
                stop_event.clear()
                movement_thread = threading.Thread(target=move_character_thread)
                movement_thread.start()
                with Listener(on_press=on_press) as listener:
                    listener.join()
                movement_thread.join()
            
            # Finalizar o programa
            case 3:
                break
    
    exit_text()
