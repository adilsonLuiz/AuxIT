import os
from Modules import validator


def check_main_module() -> int:
    print('''
            [1] - User utilits.
            [2] - Organizar Arquivos.
            [3] - Opções Trabalho.
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



def menu_work():
    """  
            Exibe um menu de opções relacionado a funções de trabalho.
    """
    clear_scream()
    print(
        '''
            [1] - Adequar maquina Recém formatada.
            [2] - Adicionar novo PowerUser.
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
    [4] - Delete All file Downloads.
    [5] - Create Random files in Desktop.
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