from .task_organizer import TaskOrganizer


class TaskScript(TaskOrganizer):
    """  
        Classe criada para manipular operações relacionada ao script.
        
    """

    def __init__(self):
        super().__init__()
        self.SHELL_NAME = 'powershell'
        self.default_name_scripts = self.get_default_name_scripts()
        self.TEMP_NAME_DIR_SCRIPTING = self.paths_user['temp'] + 'script_temp\\'
        self.create_temp_dir_to_scripting()
        self.download_script_files()

    @staticmethod
    def get_default_name_scripts():

        return [
            'installSoftware.ps1',
            'newPowerUser.ps1',
        ]

    def get_temp_name_dir_scripting(self) -> str:
        return self.TEMP_NAME_DIR_SCRIPTING

    def create_temp_dir_to_scripting(self):
        from os.path import exists

        if not exists(self.TEMP_NAME_DIR_SCRIPTING):
            self.create_dir(self.TEMP_NAME_DIR_SCRIPTING)

    def set_name_shell(self, shell_name: str):
        self.SHELL_NAME = shell_name

    def download_script_files(self):
        """  
            Realizar um request no google drive, onde estão compartilhado os arquivos auxiliares,
            para execução de tarefas na maquina, usando o powershell como auxiliar.
        """

        from google_drive_downloader import GoogleDriveDownloader as gdd

        id_files = ['1otJvFf6DjRD43KeyWTL2oHeTO-IlxCFk',
                    '1d3pgWvQ-NbXQpmFMdJrC-Bh6wJ1kIDKd',
                    ]

        for index, id_stat in enumerate(id_files):
            gdd.download_file_from_google_drive(file_id=id_stat,
                                                dest_path=self.TEMP_NAME_DIR_SCRIPTING + self.default_name_scripts[
                                                    index],
                                                )

    def execute_script(self, script_name: str):


        from os import system

        system(self.SHELL_NAME + ' ' + self.TEMP_NAME_DIR_SCRIPTING + script_name)
