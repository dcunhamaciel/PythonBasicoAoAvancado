bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')

def get_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
        for k, v in informados.items() if k in suportados)

def tab_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **novos_atrs)
    atributos = get_atrs(novos_atrs, bloco_atrs)

    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'

def tag_lista(*itens, **novos_atrs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    atributos = get_atrs(novos_atrs, ul_atrs)

    return f'<ul {atributos}>{lista}</ul>'

if __name__ == '__main__':
    print(tab_bloco('bloco'))
    print(tab_bloco('inline e classe', classe='info', inline=True))
    print(tab_bloco('inline', inline=True))
    print(tab_bloco('falhou', classe='error'))
    print(tab_bloco(tag_lista('Item 1', 'Item 2'), 'info'))
    print(tab_bloco(tag_lista, 'Sábado', 'Domingo', classe='info'))

    print(tab_bloco(tag_lista, 'Item 1', 'Item 2',
                    classe='info',
                    bloco_accesskey='m',
                    bloco_id='conteudo',
                    ul_id='lista'))
