def tab_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'

    return f'<{tag} class="{classe}">{conteudo}</{tag}>'

def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)

    return f'<ul>{lista}</ul>'

if __name__ == '__main__':
    print(tab_bloco('bloco'))
    print(tab_bloco('inline e classe', 'info', True))
    print(tab_bloco('inline', inline=True))
    print(tab_bloco('falhou', classe='error'))
    print(tab_bloco(tag_lista('Item 1', 'Item 2'), 'info'))
