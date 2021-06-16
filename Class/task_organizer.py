from Class.task_commands import TaskCommands


class TaskOrganizer(TaskCommands):
    """  
        Class que trata da parte de organização dos arquivos no programa principal.

        Atribbutes:
            DEFAULT_DIR_LIST (list): Caminho absoluto com os diretorios padrões que serão usados para mover os arquivos por categoria de extensão.
            default_extension (dict): Extensões de arquivos default.
            default_path_to_move_files (str): Armazena local onde será criado os diretorio padrões para organização dos arquivos.

    """

    def __init__(self):
        super().__init__()
        self.default_path_to_move_files = self.paths_user['document']
        self.DEFAULT_DIR_LIST = self.get_default_dir()
        self.default_extension = self.get_extension_files_default()
        self.init_default_dir()  # Checa e cria os diretorios para organização

    def get_default_dir(self):
        """ 
            Define uma lista com o caminho dos diretorios default para mover os arquivos
                Return:
                    (list): Lista com nome de diretorios.
        """
        return ([
            self.default_path_to_move_files + 'Arquivos_Texto',
            self.default_path_to_move_files + 'Arquivos_Geral',
            self.default_path_to_move_files + 'Arquivos_Multimidia',
            self.default_path_to_move_files + 'Arquivos_Imagens',
            self.default_path_to_move_files + 'Arquivos_outros'
        ]
        )

    def get_extension_files_default(self) -> dict:
        """
            Define uma estrutura padrão que contem dados relacionados a extesão de arquivos.
                Return:
                    (dict): Dicionario padrão com extensões de arquivos
        """
        return ({'texto': ['.docx', '.doc', '.txt', '.pdf'],
                 'midia': ['.mp3', '.mp4', '.wav', '.gif'],
                 'msFiles': ['.xlsx', '.xls', '.ppt', '.pps'],
                 'picture': ['.jpeg', '.mpeg']
                 }
                )

    def get_extension_files_list(self, list_file) -> list:
        """
            Extrair todas extensoes de todos arquivo dentro da lista com os arquivos,
            passada como parametro.
                Parameters:
                    list_file (list): Lista com nome dos arquivos para extrair a extensão.
                Return: 
                    Retorna uma lista composta com os nomes dos arquivos e extensões, em ordem.
        """
        # Imports
        import os

        list_extension = [[], []]
        list_file_temp = list()

        # Verificando arquivos
        for file in list_file:
            if os.path.isfile(file):
                list_file_temp.append(file)

        # Lógica para extrair extensão dos arquivos
        file_stat = str()  # varival temporaria para receber o nome e extensão dos arquivos
        for file in list_file_temp:
            # Usando a função splitext para pegar o nome e extensão
            file_stat = list(os.path.splitext(file))
            list_extension[0].append(file_stat[0])
            list_extension[1].append(file_stat[1])
        return list_extension

    def set_default_path_to_move_files(self, path: str):
        """  
            Atribui um novo valor ao diretorio padrão para mover os arquivos.
        """
        self.default_path_to_move_files = path

    def make_radom_files(self, qtd_files_to_create=5,
                         extension_file='txt',
                         path_to_create_file='desktop'
                         ) -> None:
        """
            Cria arquivos com nomes aleatorios em um diretorio informado.
                Parameters:
                    path_to_create_file (str): Keyword com o caminho para criar os arquivos
                    qtd_files_to_create (list): Quantidade de arquivos a serem criados (Default 5)
                    extension_file (str): String literal com extensão do arquivo a ser criado.

        """
        # Import
        from random import randint
        from random import choice
        from os import getcwd

        # Local var
        RAND_RANGE = 1000000
        temp_file_name = str(randint(0, RAND_RANGE))

        self.change_dir(self.paths_user[path_to_create_file])

        for file in range(qtd_files_to_create):
            # Criando arquivos
            self.create_file(temp_file_name, extension_file)
            extension_file = choice([
                'txt', 'xlsx', 'doc', 'docx', 'ppt',
                'jpeg', 'mp4', 'mp3', 'exe', 'bat', 'js'
            ]
            )
            temp_file_name = str(randint(0, RAND_RANGE))

    def init_default_dir(self) -> None:
        """  
            Cria os diretorios default do programa no CWD atual, para armazenar os arquivos organizados.
        """
        from os.path import exists
        #from os import listdir

        # Mundado para caminho padrão da criação dos diretorios.
        self.change_dir(self.default_path_to_move_files)
        for dir in self.DEFAULT_DIR_LIST:
            if exists(dir):
                pass
            else:
                self.create_dir(dir)
                print(dir)

    def organize_files(self, path_to_organize='desktop', dest_path='document') -> None:
        """
            Move arquivos para o diretorio principal, criado inicialmente pelo programa.
                Parameters:
                    path_to_organize (str): Key correspondente a estrutura de dados de diretorios padrões.
                    (Default documents user)
                        Ex: desktop, document, picture..
                    dest_path (str): Caminho destino onde os arquivos serão movidos.
        """
        from os import listdir as ls

        # Checando se o valor de parametro para o dest_path e o default ou não.
        if dest_path == 'document':
            self.change_dir(self.paths_user[path_to_organize])
        else:
            self.set_default_path_to_move_files(dest_path)
            self.change_dir(self.paths_user[path_to_organize])

        file_getting = ls()  # Coletando arquivos no CWD atual
        extension_file_getting = self.get_extension_files_list(
            file_getting)  # Obtendo uma lista em cima dos arquivos coletados
        # Usando slicing para pegar a lista de extensões apenas.
        extension_file_getting = extension_file_getting[1]

        if not extension_file_getting:
            print('Não há arquivos para serem organizados')
            exit(0)

        # Usadas no loop

        finish_file = False  # Determina o final do loop
        # Armazena a extesão que esta no atual momento da iteração
        extension_stat = extension_file_getting[0]

        while not finish_file:  # O loop ira finalizar quando a lista de extensão estiver vazia
            if extension_stat in self.default_extension['texto']:
                self.move_file_by_extension(
                    extension_stat, self.DEFAULT_DIR_LIST[0])
            elif extension_stat in self.default_extension['msFiles']:
                self.move_file_by_extension(
                    extension_stat, self.DEFAULT_DIR_LIST[1])
            elif extension_stat in self.default_extension['midia']:
                self.move_file_by_extension(
                    extension_stat, self.DEFAULT_DIR_LIST[2])
            elif extension_stat in self.default_extension['picture']:
                self.move_file_by_extension(
                    extension_stat, self.DEFAULT_DIR_LIST[3])
            else:  # Outros arquivos
                self.move_file_by_extension(
                    extension_stat, self.DEFAULT_DIR_LIST[4])

            # Update extension list
            while extension_stat in extension_file_getting:
                """  
                    Como usamos um comando para mover os arquivos de uma so vez, via prompt, temos de eliminar
                    dentro da lista de extensão, todos os arquivos com esta extensão movida, pois nesta parte da iteração
                    os aquivos desta extensão atual já foram movidas de uma so vez.
                """

                extension_file_getting.remove(
                    extension_stat)  # Removendo a extensão ja organizada no diretorio principal

            if not extension_file_getting:  # Quando a lista de exstensões estiver vazia o looping termina
                finish_file = True

            # Tenta atribuir para a variavel temporario de extensão um novo valor de extensão que exista, pós exclusão.
            try:  # Como o elemento foi excluido da lista, usamos uma constante 0 para pegar sempre o 1º indice
                extension_stat = extension_file_getting[0]
            except IndexError:
                print(f'Todos arquivos foram movidos com sucesso')
                print(
                    f'Local raiz onde arquivos estão: "{self.default_path_to_move_files}"')

    def delete_file_by_extension(self, path_to_delete_files='downloads') -> None:
        """  
            Deleta todos os arquivos existente dentro do diretorio aonde é executado.
            # TODO implementar metodo para apagar todos os diretorios e subdiretorios.
        """
        from os import remove as rm
        from os import listdir as ls
        from os.path import join

        self.change_dir(self.paths_user[path_to_delete_files])

        files_to_delete = self.get_extension_files_list(ls(self.cwd))
        files_plus_extension = list()

        for file, files in enumerate(files_to_delete[1]):
            files_plus_extension.append(
                ''.join(files_to_delete[0][file]) + ''.join(files_to_delete[1][file]))

        for file in files_plus_extension:
            rm(join(self.cwd, file))
