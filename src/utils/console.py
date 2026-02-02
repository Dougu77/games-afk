import simpleValidatorForConsoleApp.validator as validator
from pynput.keyboard import Key, KeyCode
from .keys import get_key_name
from datetime import datetime
from time import sleep

def start_text() -> None:
    print('-' * 21)
    print(f'{"-" * 5} Games AFK {"-" * 5}')
    print('-' * 21)
    print('\n-> Esse programa fica movendo seu personagem para evitar que você seja desconectado por inatividade em jogos.')
    print('-> Você pode escolher entre dois sistemas de controle: WASD ou Setas do teclado.')
    print('-> Por padrão, o sistema WASD é utilizado.')
    print('-> Para parar o programa durante sua exececução, pressione a tecla ESPAÇO.')
    print('-> Começe o programa e entre no jogo que deseja, para o programa funcionar corretamente.')

def main_menu() -> int:
    menu_title = '\nEscolha uma opção:'
    options = [
        'Trocar o sistema de controle (WASD/Setas)',
        'Iniciar o programa',
    ]
    question = 'Digite o número da opção desejada: '
    error_message = 'Opção inválida! Por favor, tente novamente.'
    return validator.validate_option(menu_title, options, question, error_message)

def choose_keys_menu() -> int:
    menu_title = '\nEscolha o sistema de controle:'
    options = [
        'WASD',
        'Setas do teclado',
    ]
    question = 'Digite o número da opção desejada: '
    error_message = 'Opção inválida! Por favor, tente novamente.'
    return validator.validate_option(menu_title, options, question, error_message)

def start_program_text() -> None:
    print('\nIniciando o programa...\n')
    for i in range(10, 0, -1):
        print(f'Começando em {i}...')
        sleep(1)
    print()

def register_movement(key: Key | KeyCode) -> None:
    print(f'{datetime.now().strftime("%H:%M:%S")} - {get_key_name(key)}')

def exit_text() -> None:
    input('\nPressione ENTER para sair...')
