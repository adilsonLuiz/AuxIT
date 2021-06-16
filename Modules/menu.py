import os
from Modules import validator


def check_main_module() -> int:
    print('''
            [1] - User utilits.
            [2] - Organize Files.
            [3] - Install softwares.
            [4] - Backups.
        '''
          )
    main_module = validator.read_option('Informe um modulo: ')
    return main_module


def banner():
    clear_scream()
    print('''\033[1;33m
    
            "██╗****██╗███████╗██╗*****██╗******██████╗*██████╗*███╗***███╗███████╗****████████╗*██████╗******█████╗*██╗***██╗██╗**██╗██╗████████╗*****██╗****██████╗*";
            "██║****██║██╔════╝██║*****██║*****██╔════╝██╔═══██╗████╗*████║██╔════╝****╚══██╔══╝██╔═══██╗****██╔══██╗██║***██║╚██╗██╔╝██║╚══██╔══╝****███║***██╔═████╗";
            "██║*█╗*██║█████╗**██║*****██║*****██║*****██║***██║██╔████╔██║█████╗*********██║***██║***██║****███████║██║***██║*╚███╔╝*██║***██║*******╚██║***██║██╔██║";
            "██║███╗██║██╔══╝**██║*****██║*****██║*****██║***██║██║╚██╔╝██║██╔══╝*********██║***██║***██║****██╔══██║██║***██║*██╔██╗*██║***██║********██║***████╔╝██║";
            "╚███╔███╔╝███████╗███████╗███████╗╚██████╗╚██████╔╝██║*╚═╝*██║███████╗*******██║***╚██████╔╝****██║**██║╚██████╔╝██╔╝*██╗██║***██║********██║██╗╚██████╔╝";
            "*╚══╝╚══╝*╚══════╝╚══════╝╚══════╝*╚═════╝*╚═════╝*╚═╝*****╚═╝╚══════╝*******╚═╝****╚═════╝*****╚═╝**╚═╝*╚═════╝*╚═╝**╚═╝╚═╝***╚═╝********╚═╝╚═╝*╚═════╝*";
            "*********************************************************************************************************************************************************";
        \033[m'''
          )


def menu_suit():
    """  
        Exibe um menu de opções relacionado a funções de instalação de softwares.
    """
    clear_scream()
    print(
        '''
            [1] - Configurar maquina recem formatada.
        '''
    )


def menu_user():
    """  
        Imprime um menu com opções relacionada a operações com usuario local.
    """
    print(
        '''
    [1] - Add new user.
    [2] - Remove user.
    [3] - Change Password.
        '''
    )


def menu_files():
    clear_scream()
    print(
        '''
    [1] - Organize Desktop Files.
    [2] - Organize Downloads Files.
    [3] - Organize Documents Files.
    [4] - Delete All file Downloads (Delete all files in downloads).
    [5] - Create Random files in Desktop(For testing).
        '''
    )


def menu_backup():
    clear_scream()
    print(
        '''
        [1] - Backup de usuário atual.
        [2] - Backup de outro usuário.
        '''
    )


def clear_scream():
    os.system('cls || clear')
