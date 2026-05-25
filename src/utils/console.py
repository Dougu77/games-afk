# Imports
import simpleValidatorForConsoleApp.validator as validator
from pynput.keyboard import Key, KeyCode
from .keys import get_key_name
from datetime import datetime
from time import sleep

# Funções
def start_text() -> None:
    print('-' * 21)
    print(f'{"-" * 5} Games AFK {"-" * 5}')
    print('-' * 21)
    print('\n-> Esse programa faz diversas coisas em AFK para você.')
    print('-> Você pode se mover sozinho, escolha entre dois sistemas de movimentação: WASD ou Setas do teclado.')
    print('-> Por padrão, o sistema WASD é utilizado.')
    print('-> Você pode deixar o botão esquerdo do mouse pressionada.')
    
    print('-> Para parar o programa durante sua exececução, pressione a tecla ESPAÇO.')
    print('-> Começe o programa e entre no jogo que deseja, para o programa funcionar corretamente.')

def main_menu() -> int:
    menu_title = '\nEscolha uma opção:'
    options = [
        'Trocar o sistema de movimentação (WASD/Setas)',
        'Iniciar a movimentação',
        'Iniciar o botão esquerdo do mouse',
        'Finalizar o programa',
    ]
    question = 'Digite o número da opção desejada: '
    error_message = 'Opção inválida! Por favor, tente novamente.'
    return validator.validate_option(menu_title, options, question, error_message)

def choose_keys_menu() -> int:
    menu_title = '\nEscolha o sistema de movimentação:'
    options = [
        'WASD',
        'Setas',
    ]
    question = 'Digite o número da opção desejada: '
    error_message = 'Opção inválida! Por favor, tente novamente.'
    return validator.validate_option(menu_title, options, question, error_message)

def start_count_text() -> None:
    for i in range(10, 0, -1):
        print(f'Começando em {i}...')
        sleep(1)
    print()

def register_movement(key: Key | KeyCode) -> None:
    print(f'{datetime.now().strftime("%H:%M:%S")} - {get_key_name(key)}')

def exit_text() -> None:
    input('\nPressione ENTER para sair...')
