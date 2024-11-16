def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')

    conteudo = ''.join(args)
    atributos = ' '.join(f'{nome}="{valor}"' for nome, valor in kwargs.items())

    return f'<{tag} {atributos}>{conteudo}</{tag}>'

if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf', name='JF'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert'
        )
    )
