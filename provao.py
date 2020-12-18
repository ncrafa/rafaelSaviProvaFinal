listaUsuarios=["cleber","joao"]
def cadastro():
    texto = "Objetos a serem emprestados{} \n Objetos que ja foram emprestados{} "
    cadastrar=0
    opcao = 1
    while  opcao  ==  1 :
        print ( "Digite 1 para realizar novo cadastro?" )
        print ( "Digite 2 caso você seja um usuario ja cadastrado" )
        operacao2  =  int ( input ( "Deseja realizar qual operação:"))
        if operacao2 == 1:
            usuario = input("Seu nome: ")
            while(len(usuario)<3):
                print ( "O nome deve conter no mínimo 3 letras " )
                usuario = input(" Digite novamente seu nome: ")
            usuario=usuario.upper()
            if usuario in listaUsuarios:
                print('Este usuario ja esta cadastrado,insira outro nome')
            else:
                print('Usuário cadastrado com sucesso')
                listaUsuarios.append(usuario)
            opcao = 0
        if operacao2 == 2:
            usuario = input("Seu nome: ")
            if usuario in listaUsuarios:
                print('Usuário encontrado')
            else:
                print("usuario não encontrado")
            opcao=0
def emprestar():
    listaDatas=[]
    listaDatasObjetos=[]
    listaAmbos=[listaDatas,listaDatasObjetos]
    coisasParaEmprestar = ["livro","boneca"]
    coisasJaEmprestadas = ["isqueiro","mandioca"]
    coisasJaEmprestadasComNomes = [coisasJaEmprestadas,listaUsuarios] 
    escolha = 1
    print("objetos a serem emprestados: \n",coisasParaEmprestar)
    print("objetos emprestados pelos respectivos usuários: \n",coisasJaEmprestadasComNomes)
    while  escolha  ==  1 :
        print ( "Digite 1 para Emprestar algum objeto" )
        print ( "Digite 2 para  pegar emprestado algum objeto" )
        operacao  =  int ( input ( "Deseja realizar qual operação:"))
        if operacao == 1:
            objetoEmprestar = input("Qual o nome do objeto a ser emprestado ")
            coisasParaEmprestar.append(objetoEmprestar)
            print("Objeto cadastrado \n lista de objetos disponíveis para serem emprestados \n ",coisasParaEmprestar)
        if operacao == 2:
            print("Disponíveis  \n ",coisasParaEmprestar)
            objetoPegar = input("Qual o nome do objeto que você deseja pegar? ")
            if objetoPegar in coisasParaEmprestar:
                print("Empréstimo feito com sucesso")
                dataDevolucao = input("Para finalizar, digite a data de devolução: \n")
                listaDatas.append(dataDevolucao)
                listaDatasObjetos.append(objetoPegar)
                val_remove = objetoPegar
                if val_remove in coisasParaEmprestar:
                    coisasParaEmprestar.remove(val_remove)
                    print("lista atualizada dos objetos disponiveis para empréstimo \n",coisasParaEmprestar)
            else:
                print("não foi possivel realizar a operação, pois o objeto nao foi encontrado")   
        continuar = int(input("deseja realizar alguma operação novamente?\n 1- sim\n2 - não"))
        print("lista de objetos disponíveis para serem emprestados \n ",coisasParaEmprestar)
        print("Objetos que serão devolvidos: \n ",listaAmbos)
        if continuar == 1:
            escolha = 1
        else:
            escolha=0   


cadastro()
emprestar()




