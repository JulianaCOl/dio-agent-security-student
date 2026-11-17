import sqlite3
import os

# Função para inicializar um banco de dados de testes rápido (caso não exista)
def setup_database():
    if os.path.exists('users.db'):
        os.remove('users.db')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Cria uma tabela de usuários simples
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    
    # Insere um usuário de teste
    cursor.execute("INSERT INTO users (username, password, role) VALUES ('admin', 'senha123', 'administrator')")
    cursor.execute("INSERT INTO users (username, password, role) VALUES ('joao', 'abc456', 'user')")
    
    conn.commit()
    conn.close()

# Função VULNERÁVEL de login (alvo da nossa análise com o agente)
def login_vulneravel(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILIDADE CRÍTICA: Concatenação direta de strings na query SQL
    # Um invasor pode digitar ' OR '1'='1 no campo de usuário para burlar a autenticação.
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    print(f"\n[DEBUG] Query executada: {query}")
    
    try:
        cursor.execute(query)
        user = cursor.fetchone()
    except Exception as e:
        print(f"[ERRO SQL] {e}")
        user = None
        
    conn.close()
    return user

if __name__ == "__main__":
    # Prepara o banco de laboratório
    setup_database()
    
    print("=== TESTE DE LOGIN VULNERÁVEL (LAB) ===")
    
    # Teste legítimo
    print("\nTentativa 1: Login correto (admin / senha123)")
    resultado = login_vulneravel("admin", "senha123")
    if resultado:
        print(f"Sucesso! Bem-vindo, {resultado[1]} (Cargo: {resultado[3]})")
    else:
        print("Falha no login.")

    # Teste malicioso (SQL Injection clássico)
    print("\nTentativa 2: Tentativa de SQL Injection (' OR '1'='1)")
    resultado_malicioso = login_vulneravel("admin' OR '1'='1", "senha_falsa")
    if resultado_malicioso:
        print(f"ALERTA! Acesso burlado com sucesso! Logado como: {resultado_malicioso[1]} (Cargo: {resultado_malicioso[3]})")
    else:
        print("Login bloqueado.")