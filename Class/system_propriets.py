class SystemPropriets(object):
    """
    Classe para armazenar e gerenciar atributos do sistema.
    Também possui metodos para configuração de caminhos usados pelo programa principal.
    """

    def __init__(self):
        """Inicializa os atributos basicos da classe, usado por ela mesma e seus herdeiros.

            Attributes:
                HOSTNAME (str): Armazena o nome do usuário logado no sistema.
                PATH_USERS_LIST (str): Armazena o diretorio raiz onde estão os diretorios de cada usuário.
                USER_SYSTEM_NAME (list): Pega todos usuários com diretorios ja criados.
                ALL_USER_DIR (list): Constante armazena  o nome do diretorio de cada usuário.
                paths_user (dict):  Armazena  o caminho de diretorio do usuário logado no momento.
                paths_system (dict): Armazena o caminho para diretorio de sistema.
                ARCH (str): Arquitetura operacional da maquina.
                cwd (str): Armazena o cwd atual no momento da execução.
                time_system (str): Horario atual do sistema
                date_system (str): Data atual do sistema
        """
        # Atributos de instancia da classe
        self.HOSTNAME = self.set_login()
        self.PATH_USERS_LIST = 'C:\\Users\\'
        self.USER_SYSTEM_NAME = self.get_all_user()
        self.paths_user = self.get_path_user()
        self.paths_system = self.set_path_system()
        self.ALL_USER_DIR = self.get_all_user()
        self.ARCH = self.get_architecture()
        self.cwd = self.get_cwd()
        self.time_system = self.get_time_system()
        self.date_system = self.get_date_system()

    @staticmethod
    def get_date_system() -> str:
        from datetime import date
        dateNow = date.today()
        return dateNow.strftime('%d-%m-%y')

    @staticmethod
    def get_time_system() -> str:
        from datetime import datetime
        timeNow = datetime.now()
        return timeNow.strftime('%H_%M')

    @staticmethod
    def get_architecture() -> str:
        from platform import architecture
        return architecture()[0]

    def get_all_user(self) -> list:
        """Coleta dentro do OS uma lista com o nome de todos os usuários que possuam diretorio,
        ja existente dentro do sistema.

            Return 
                (list) Nome de usuários dentro do sistema
        """
        from os import listdir as ls

        user_not_list = [
            'All Users', 'Default', 'Default User',
            'desktop.ini', 'Public', 'Todos os Usuários',
            'Usuário Padrão'
        ]  # Usuarios que não serão listados, padrão do OS windows

        return [user for user in ls(self.PATH_USERS_LIST) if user not in user_not_list]

    @staticmethod
    def get_cwd() -> str:
        """
        Coleta do sistema o CWD atual.
            Return
                (list) Com o diretorio atual.
        """
        from os import getcwd

        return getcwd()

    def set_cwd(self, path) -> None:
        self.cwd = path

    def set_path_system(self) -> list:
        # Caminhos básicos para arquivos de configuração windows
        paths_system = {
            'rootSys': 'C:\\',
            'winDir': 'C:\\Windows\\',
            'pf': 'C:\\Program Files\\',
            'pf86': 'C:\\Program Files (x86)\\',
        }

        return paths_system

    def get_path_user(self) -> list:
        """ Configura caminhos padrões usado pelo programa principal.
            Return
                path_user (dict): Caminhos defualt pré definido na função.  

        """
        path_user = {
            'desktop': 'C:\\Users\\' + self.HOSTNAME + '\\Desktop\\',
            'document': 'C:\\Users\\' + self.HOSTNAME + '\\Documents\\',
            'music': 'C:\\Users\\' + self.HOSTNAME + '\\Music\\',
            'downloads': 'C:\\Users\\' + self.HOSTNAME + '\\Downloads\\',
            'picture': 'C:\\Users\\' + self.HOSTNAME + '\\Picture\\',
            'applocal': 'C:\\Users\\' + self.HOSTNAME + '\\AppData\\Local\\',
            'startup': 'C:\\Users\\' + self.HOSTNAME + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programas\\',
            'temp': 'C:\\Users\\' + self.HOSTNAME + '\\AppData\\Local\\Temp\\',
            'homeUser': 'C:\\Users\\' + self.HOSTNAME + '\\',
            'appdata': 'C:\\Users\\' + self.HOSTNAME + '\\AppData\\'
        }
        return path_user

    @staticmethod
    def set_login() -> str:
        from os import getlogin

        return getlogin()

    def __str__(self):
        return(
            f'''
            Hostname: {self.HOSTNAME}
            CWD: {self.cwd}
            '''
        )
