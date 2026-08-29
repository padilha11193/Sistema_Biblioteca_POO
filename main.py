class Livro:
    def __init__ (self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            print("Livro emprestado com sucesso!")
        else:
            print("Livro já foi emprestado por outro usuário.")

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")
        if not self.emprestado:
            print("Status: disponível para empréstimo")
        else:
            print("Status: emprestado")

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            print("Livro devolvido com sucesso!")
        else:
            print("Esse livro já está disponível.")

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self):
        titulo = input("Informe o título do livro: ")
        autor = input("Informe o(a) autor(a) do livro: ")
        paginas = int(input("Informe o número de páginas: "))

        livro = Livro(titulo, autor, paginas)
        self.livros.append(livro)
        print(f'"{livro.titulo}" adicionado à biblioteca.')

    def listar_livros(self):
        print("--- Lista de livros catalogados na biblioteca ---")
        for livro in self.livros:
            print("-" * 30)
            livro.mostrar_info()
            print()

    def emprestar_livro(self):
        encontrado = False
        titulo = input("Digite o título do livro a ser emprestado:\n")
        for livro in self.livros:
            if titulo == livro.titulo:
                encontrado = True
                livro.emprestar()

        if not encontrado:
            print("Livro não encontrado no sistema.")   
    
    def devolver_livro(self):
        encontrado = False
        titulo = input("Digite o título do livro:\n")
        for livro in self.livros:
            if titulo == livro.titulo:
                encontrado = True
                livro.devolver()

        if not encontrado:
            print("Livro não encontrado no sistema.")  

    def buscar_livro(self):
        encontrado = False
        titulo = input("Digite o título do livro:\n")
        for livro in self.livros:
            if titulo == livro.titulo:
                encontrado = True
                livro.mostrar_info()

        if not encontrado:
            print("Livro não encontrado no sistema.")

biblioteca = Biblioteca()

while True:
    print("\n1 - Adicionar livro ao acervo")
    print("2 - Exibir acervo completo")
    print("3 - Buscar livro")
    print("4 - Emprestar livro")
    print("5 - Devolver livro")
    print("6 - Sair do sistema")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        biblioteca.adicionar_livro()
    elif opcao == "2":
        biblioteca.listar_livros()
    elif opcao == "3":
        biblioteca.buscar_livro()
    elif opcao == "4":
        biblioteca.emprestar_livro()
    elif opcao == "5":
        biblioteca.devolver_livro()
    elif opcao == "6":
        break

    else:
        print("\nComando não identificado, tente novamente.")
        continue
