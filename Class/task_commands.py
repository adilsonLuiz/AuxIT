from Class.system_propriets import SystemPropriets


class TaskCommands(SystemPropriets):
    """  
    Classe para representar uma interface shell, 
    para execução de comandos.
    Contém comandos pré definidos para execução de tarefas no programa.
    """

    def __init__(self):
        super().__init__()
    
    @staticmethod
    def add_user() -> None:
        """  
            Adiciona um novo usuario ao sistema via shell.
        """
        from os import system as cmd

        name = input('Nome do usuário: ')
        passwd = input('Senha: ')

        cmd(f'net user "{name}" {passwd} /add')


    def remove_user(self) -> None:
        """  
        Delete um usuario do sistema.
        """
        from os import system as cmd

        self.list_users()
        name = input('Usuário a remover(Digite o nome): ')
        cmd(f'net user "{name}" /delete')


    def change_passwd(self) -> None:
        """Lista os usuários no OS e muda a senha baseado, na escolha do usuário.
        """
        from os import system as cmd

        self.list_users()
        username = input('Informe usuário a mudar senha: ')
        cmd(f'net user {username} *')


    def list_users(self) -> None:
        """  
            Exibe usuários existentes no OS.
        """

        from os import system as cmd

        cmd('cls')
        print('List of user in sistem')
        print('-=' * 10)
        for user in self.USER_SYSTEM_NAME:
            print(f'Usuário: {user}')
        print('-=' * 10)

    def create_dir(self, path_dir: str) -> None:
        """  
        Cria um diretorio no CWD atual.
            Parameters:
                path_dir (str): Caminho ou nome do diretorio.
        """

        from os import makedirs

        makedirs(path_dir)

    def copy_file_by_extension(self, extension: str, dest_path: str) -> None:
        """  
            Copia todos os arquivos existente no CWD por sua extensão.
                Parameters:
                    extension (str): Extesão do arquivo.
                    dest_path (str): Caminho alvo para enviar as copias.
        """
        from os import system as cmd

        cmd(f'copy *.{extension} {dest_path}')

    def create_file(self, name_file: str, extension: str) -> None:
        """  
        Cria arquivos no CWD atual.
            Parameters:
                name_file (str): Nome do arquivo a ser criado.
                extension (str): Extensão do arquivo a ser criado.
        """
        from os import system as cmd

        cmd(f'echo >> {name_file}.{extension}')

    def move_file_by_extension(self, extension: str, dest_path: str) -> None:
        """  
            Move todos os arquivos no CWD atual pela extensão, para um destino.
                Parameters:
                    extension (str): Extensão do arquivo a ser movido.
                    dest_path (str): Caminho destino para mover arquivos.
        """
        from os import system as cmd

        file_to_move = self.cwd + '*' + extension  # arquivo origen
        cmd(f'powershell move-item -Force {file_to_move} "{dest_path}"')

    def change_dir(self, path: str) -> None:
        """  
            Muda o CWD atual para outro especificado.
             Parameters:
                path (str): Caminho destino para mudança.
        """
        from os import chdir

        self.cwd = path
        chdir(path)

    def delete_all_file(self, abs_path: str):
        """  
            Deleta todos os diretorios, subdiretorios e arquivos.

            Parameters:
                abs_path (str): Caminho absoluto do diretorio
        """
        from os import system as cmd
        cmd(f'rmdir {abs_path} /q /s')
