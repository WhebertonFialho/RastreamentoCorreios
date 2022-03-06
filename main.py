from colorama import Fore, Style, init
from correios import Correios

CODIGOS_RASTREAMENTO = ['JN860049042BR', 'JN557761475BR', 'JN051779015BR']

init()
correios = Correios()

print('-' * 75)

for cod_rastreio in CODIGOS_RASTREAMENTO:
    objeto = correios.rastreio(cod_rastreio)
    
    print('Cod. Rastreamento: ' + Fore.GREEN + cod_rastreio + Style.RESET_ALL)
    print('-' * 75)
    
    for evento in objeto.eventos:
        print('Data: ', end = '')
        print(Fore.LIGHTYELLOW_EX + evento.data, end = Style.RESET_ALL)
        
        print(' Localidade:' + Fore.LIGHTBLUE_EX + evento.unidade.cidade, end = Style.RESET_ALL)
       
        print(' Descrição: ' + Fore.YELLOW + evento.descricao + Style.RESET_ALL)
    
    print('-' * 75)
