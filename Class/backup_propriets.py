
from Class.task_organizer import TaskOrganizer

class BackupPropriets(TaskOrganizer):
    """  
        Ira possuir propriedades realacionada a entidade backup
        
        Attributes:
            percent_backup (int): Armazena o percentual atual do backup ja realizado
            backup_finish (bool): Armazena um bool, para indicar se o backup finalizou
            report_error_backup (dict): Armazena um dict, para estruturar os erros durante o processo de backup
            compress_backup (bool): Armazena um bool, indicando se o backup vai ser comprimido
            backup_to_mail (bool): Chave para verificar se backup vai ser enviado por e-mail.
    """
    def __init__(self):
        super().__init__()
        self.dir_source_backup = self.paths_user['homeUser'] # Diretorio inicial do user
        self.dir_dest_backup = self.paths_user['homeUser']
        self.backup_file_name = 'Backup' + self.HOSTNAME.upper() + self.time_system \
        + '_' + self.date_system
        self.full_backup = False
        self.percent_backup = 0
        self.backup_finish = False
        self.report_error_backup = {}
        self.compress_backup = True
        self.backup_to_mail = False
        self.cont_files_backup = 0
        self.cont_dir_backup = 0
        self.size_backup = 0
        self.restrict_files_backup = []
        self.restrict_dir_backup = []


    def get_source_path_backup(self):
        return self.dir_source_backup
    
    def get_dest_path_backup(self):
        return self.dir_dest_backup
    
    def get_backup_file_name(self):
        return self.backup_file_name

    def get_cont_files_backup(self):
        return self.cont_files_backup
    
    def get_cont_dir_backup(self):
        return self.cont_dir_backup
    
    def get_size_backup(self):
        return self.size_backup
    
    def set_file_name_backup(self, name: str):
        self.backup_file_name = name

    def set_dest_path_backup(self, path: str):
        self.dir_dest_backup = path
    
    def set_source_path_backup(self, path: str):
        self.dir_source_backup = path

    def set_restrict_files_to_backup(self, file_name:str):
        self.restrict_files_backup.append(file_name)
    
    def set_restrict_dir_to_backup(self, dir_name: str):
        self.restrict_dir_backup.append(dir_name)






