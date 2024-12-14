from datetime import datetime
from loja import Cliente, Vendedor, Compra

def main():
    cliente = Cliente('Maria Lima', 44)
    vendedor = Vendedor('Pedro Garrido', 36, 5000)

    compra_1 = Compra(vendedor, datetime.now(), 512)
    compra_2 = Compra(vendedor, datetime(2018, 6, 4), 256)

    cliente.registrar_compra(compra_1)
    cliente.registrar_compra(compra_2)

    valor_total = cliente.total_compras()
    qtd_compras = len(cliente.compras)

    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto else '')
    print(f'Vendedor: {vendedor}')
    print(f'Total: {valor_total} em {qtd_compras}')
    print(f'Última compra: {cliente.get_data_ultima_compra()}')

if __name__ == '__main__':
    main()
