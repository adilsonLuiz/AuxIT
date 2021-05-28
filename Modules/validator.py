from Modules import menu
from Class.task_commands import TaskCommands
from Class.task_organizer import TaskOrganizer

def read_option(op):
    while True:
        try:
            valor = int(input(op))
        except ValueError:
            print('Somente numeros')
        else:
            return valor


def read_submodule(menu_print) -> int:
    if menu_print == 'user':
        menu.menu_user()
        return read_option('informe um modulo: ')
    elif menu_print== 'files':
        menu.menu_files()
        return read_option('Informe um modulo: ')

def check_modules_options(main_module):
    if main_module == 1: # User option
        user = TaskCommands()
        sub_module = read_submodule('user')
        if sub_module == 1:
            user.add_user()
        elif sub_module == 2:
            user.remove_user()
        elif sub_module == 3:
            user.change_passwd()
    elif main_module == 2: # Files
        files = TaskOrganizer()
        sub_module = read_submodule('files')
        if sub_module == 1:
            files.organize_files()
        

t = TaskOrganizer()

