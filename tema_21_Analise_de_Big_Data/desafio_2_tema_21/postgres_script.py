import psycopg2
from psycopg2 import sql

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname='your_database_name',
    user='your_username',
    password='your_password',
    host='localhost',
    port='5432'
)

# Criar um cursor
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER
)
''')

# Inserir dados
cursor.execute('''
INSERT INTO users (name, age) VALUES (%s, %s)
''', ('Alice', 30))

cursor.execute('''
INSERT INTO users (name, age) VALUES (%s, %s)
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
UPDATE users SET age = %s WHERE name = %s
''', (31, 'Alice'))

# Deletar dados
cursor.execute('''
DELETE FROM users WHERE name = %s
''', ('Bob',))

# Commit e fechar a conexão
conn.commit()
conn.close()
