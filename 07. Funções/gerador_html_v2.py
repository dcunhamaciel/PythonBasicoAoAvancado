def tab_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'

    return f'<{tag} class="{classe}">{texto}</{tag}>'

if __name__ == '__main__':
    print(tab_bloco('bloco'))
    print(tab_bloco('inline e classe', 'info', True))
    print(tab_bloco('inline', inline=True))
    print(tab_bloco('falhou', classe='error'))
