from Modules import menu
from Class.task_commands import TaskCommands
from Class.task_organizer import TaskOrganizer
from Class.task_backup import TaskBackup

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
    elif menu_print == 'backup':
        menu.menu_backup()
        return read_option('Informe um modulo: ')

def check_modules_options(main_module):
    """  
        Executa os modulos do programa com base na escolha do modulo principal
    """
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
        elif sub_module == 2:
            files.organize_files('downloads')
        elif sub_module == 3:
            files.organize_files('document')
        elif sub_module == 4:
            # TODO criar logica para apagar pastas.
            files.delete_file_by_extension()
        elif sub_module == 5:
            files.make_radom_files()
    elif main_module == 4: # Backup module
        backup = TaskBackup()
        sub_module = read_submodule('backup')
        if sub_module == 1:
            backup.check_backup_properties()
            backup.execute_backup()



        



