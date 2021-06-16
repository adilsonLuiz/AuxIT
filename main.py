# -*- coding: utf-8 -*-

from os import system
from Modules import menu
from Modules import validator


# TODO repensar na função do programa principal
# TODO A ideia e dar as opçoes disponiveis para o usuario e ele escolher uma delas


while True:
    try:
        menu.banner()
        main_module = menu.check_main_module()
        validator.check_modules_options(main_module)
    except KeyboardInterrupt:
        print('Encerrando programa.')
        exit(0)
