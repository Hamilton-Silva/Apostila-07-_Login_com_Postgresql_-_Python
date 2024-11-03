import psycopg

# Classe para representar o usuário
class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

# Função para verificar se o usuário existe no banco de dados
def existe(usuario):
    try:
        # Conecta ao banco de dados PostgreSQL
        with psycopg.connect(
            host="localhost",
            dbname="pbdi",
            user="postgres",
            password="123456"
        ) as conexao:
            # Cria um cursor para executar comandos SQL
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT 1 FROM tb_usuario WHERE login = %s AND senha = %s",
                    (usuario.login, usuario.senha)
                )
                # Verifica se encontrou algum registro
                return cursor.fetchone() is not None
    except Exception as e:
        print(f"Erro ao verificar usuário: {e}")
        return False

# Função para inserir um novo usuário no banco de dados
def insere(usuario):
    try:
        # Conecta ao banco de dados PostgreSQL
        with psycopg.connect(
            host="localhost",
            dbname="pbdi",
            user="postgres",
            password="123456"
        ) as conexao:
            # Cria um cursor para executar comandos SQL
            with conexao.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tb_usuario (login, senha) VALUES (%s, %s)",
                    (usuario.login, usuario.senha)
                )
                # Confirma a transação
                conexao.commit()
                return True
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
        return False

# Função para exibir o menu e tratar as opções do usuário
def menu():
    texto = "\n0-Fechar\n1-Login\n2-Logoff\n3-Inserir Usuário\nEscolha uma opção: "
    usuario = None
    while True:
        try:
            op = int(input(texto))
            if op == 0:
                print("Até mais")
                break
            elif op == 1:
                login = input("Digite seu login: ")
                senha = input("Digite sua senha: ")
                usuario = Usuario(login, senha)
                print("Usuário OK!" if existe(usuario) else "Usuário NOK!")
            elif op == 2:
                usuario = None
                print("Logoff realizado com sucesso")
            elif op == 3:
                login = input("Digite o login: ")
                senha = input("Digite a senha: ")
                usuario = Usuario(login, senha)
                if insere(usuario):
                    print("Usuário cadastrado com sucesso")
                else:
                    print("Ocorreu um erro ao cadastrar o usuário")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Função principal
def main():
    menu()

if __name__ == "__main__":
    main()
