# coding: utf-8

import import_string


def configure(app):
    """Extension Factory, carrega as extensoes definidas em
    app.config.EXTENSIONS
    """
    for extension in app.config.get('EXTENSIONS', []):
        try:
            factory = import_string(extension)
            factory(app)
        except Exception as e:
            app.logger.error(f'Erro ao carregar {extension}: {e}')
        else:
            app.logger.debug(f'Extensao {extension} carregada com sucesso!')
