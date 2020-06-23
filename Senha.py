senha = 'vitorduarte'
acesso=''
print('Para acessar digite sua senha:')

while acesso != senha:
    acesso=input()
    print('senha errada')
    if acesso == senha:
        print('Bem vindo')
