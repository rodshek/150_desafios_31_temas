import sqlite3

# Conectar ao banco de dados (ou criar um novo banco de dados)
conn = sqlite3.connect('example.db')

# Criar um cursor
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Inserir dados
cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Bob', 25))

# Commit das alterações
conn.commit()

# Consultar dados
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print('Data in table:')
for row in rows:
    print(row)

# Atualizar dados
cursor.execute('''
UPDATE users SET age = ? WHERE name = ?
''', (31, 'Alice'))

# Deletar dados
cursor.execute('''
DELETE FROM users WHERE name = ?
''', ('Bob',))

# Commit e fechar a conexão
conn.commit()
conn.close()
