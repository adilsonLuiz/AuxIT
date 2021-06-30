from Class.backup_propriets import BackupPropriets
from Modules import validator


class TaskBackup(BackupPropriets):
    """  
        Gerencia todas as tarefas de execução do backup.

        Attributes:
            percent_backup (int): Armazena o percentual atual do backup ja realizado
            files_to_backup (list): Recebe uma list com todos os nome de diretoros para backup
            backup_name_now (str): Armazena o nome atual escolhido para o arquivo do backup no momento

        TODO
            - Implementar metodo de enviar backup por e-mail
            - Verificar erro no nome do arquivo comprimido
            - Implementar metodo de porcentagem total do backup
            - Remodelar print durante execução do backup
            - Implementar metodo para salvar erros durante execução do backup
            - Implementar metodo para escolher o usuário a ser feito o backup
            - Implementar metodo para realizar o backup de todos usuarios existentes no sistema
    """

    def __init__(self):
        super().__init__()
        self.files_to_backup = self.get_data_to_backup_home()
        self.backup_name_now = self.get_backup_file_name()
        self.create_backup_dir()

    def get_data_to_backup_home(self) -> list:
        """  
            Define todos os arquivos e diretorios 
            que serão salvos no diretorio raiz do usuario.
        """

        from os import listdir

        #TODO criar logica para pegar todas as pastas
        home_files_backup = [
            'Desktop', 'Downloads', 'Documents',
            'Videos', 'Pictures', 'AppData\\Roaming',
        ]
        self.change_dir(self.paths_user['appdata'])

        # Check key folder insider AppData\Local\
        for content in listdir(self.paths_user['applocal']):
            if content == 'Google':
                home_files_backup.append('AppData\\Local\\' + content)
            elif content == 'Microsoft':
                home_files_backup.append('AppData\\Local\\' + content)
            elif content == 'Programs':
                home_files_backup.append('AppData\\Local\\' + content)

        return home_files_backup

    def set_percent_backup(self, valuer: int):
        self.percent_backup = valuer

    def compress_backup_file(self, path_archive: str, path_save_file=None):
        import shutil
        # TODO Verificar por que nome de backup esta vindo user\hostname\backup

        # Mudando o CWD, onde o arquivo será salvo
        if not path_save_file:
            self.change_dir(self.paths_user['desktop'])
        else:
            self.change_dir(path_save_file)

        shutil.make_archive(self.backup_name_now, 'zip',
                            base_dir=path_archive,
                            root_dir=self.paths_user['desktop']
                            )  # Criando ZIP file do backup

    def send_backup_file_to_mail(self, mail_adress: str, mail_password: str):
        # TODO enviar o arquivo de backup por email
        pass

    def create_backup_dir(self):
        from os import makedirs
        from os.path import exists

        path_backup = self.dir_dest_backup + self.backup_name_now
        if not exists(path_backup):
            makedirs(path_backup)
        else:
            pass

    def check_backup_properties(self):
        """  
            Coleta do usuário propriedades basicas sobre execução do backup
        """
        bkp_compress = validator.read_option(
            'Comprimir backup[1 - Sim 2 - Não]: ')
        if bkp_compress == 1:
            self.compress_backup = True
        else:
            self.compress_backup = False

    def do_backup(self):
        """  
            Realiza um backup.
        """
        import shutil
        from os.path import join

        # Junta o diretorio abs de destino o nome do backup para criar um diretorio abs destino.
        dest_path = self.dir_dest_backup + self.backup_file_name + '\\'

        for file in self.files_to_backup:
            # Pega o diretorio base de origem e junta com o nome do diretorio.
            file_to_backup = self.dir_source_backup + file
            print(f'{file_to_backup} -> {dest_path + file}')
            try:
                shutil.copytree(join(self.dir_source_backup,
                                file), join(dest_path, file))
            except shutil.Error:
                pass
            except PermissionError:
                pass


    def execute_backup(self):
        import shutil
        from os.path import join

        # Junta o diretorio abs de destino o nome do backup para criar um diretorio abs destino.
        dest_path = self.dir_dest_backup + self.backup_file_name + '\\'

        print('Realizando backup....')
        self.do_backup()

        if self.compress_backup:
            try:
                self.compress_backup_file(dest_path)
            except ValueError:
                pass
            finally:
                print('Backup Finalizado')

        # TODO excluir diretorio de backup do HD
