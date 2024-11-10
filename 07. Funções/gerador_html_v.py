def tab_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'

if __name__ == '__main__':
    # Testes (assertions)
    assert tab_bloco('Incluído com sucesso!') == '<div class="success">Incluído com sucesso!</div>'
    assert tab_bloco('Impossível excluir!', 'error') == '<div class="error">Impossível excluir!</div>'

    print(tab_bloco('bloco'))
