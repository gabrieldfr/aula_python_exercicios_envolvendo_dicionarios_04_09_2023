palavra_key = {'python': 'linguagem de alta performance', 'machine learning': 'Técnica de aprendizado de máquina'}


print('Tópico:')
for v in palavra_key.keys():
    print(v)
user_choice = input('Selecione um tópico: ').lower()

definicao = palavra_key.get(user_choice, 'Palavra-chave não encontrada')
print(f'{user_choice}: {definicao}')
