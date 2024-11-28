import psycopg
from psycopg.types.json import Jsonb

# Configuração do banco de dados
DB_CONFIG = {
    "dbname": "petdatabase",
    "user": "edb_admin",
    "password": "Upandcoming92@",
    "host": "p-r5xhpcs8oh.pg.biganimal.io",
    "port": 5432  # Porta padrão do PostgreSQL
}

def connect():
    """
    Estabelece a conexão com o banco de dados usando as configurações definidas.
    """
    try:
        return psycopg.connect(**DB_CONFIG)
    except psycopg.OperationalError as e:
        print("Erro ao conectar ao banco de dados:", e)
        raise

def create_table():
    """
    Cria a tabela 'cadastropet' no banco de dados, se não existir.
    """
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cadastropet (
                    id SERIAL PRIMARY KEY,
                    nome TEXT,
                    telefone TEXT,
                    email TEXT,
                    nomepet TEXT,
                    statuspet TEXT,
                    especiepet TEXT,
                    racapet TEXT,
                    corpet TEXT,
                    localizacaopet TEXT,
                    datapet DATE,
                    infoadicionalpet TEXT,
                    imagempet TEXT,
                    aprovado INTEGER DEFAULT 0
                )
            """)
            conn.commit()

def update_table_schema():
    """
    Adiciona a coluna 'aprovado' à tabela 'cadastropet', se ela não existir.
    """
    with connect() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("ALTER TABLE cadastropet ADD COLUMN aprovado INTEGER DEFAULT 0")
                conn.commit()
            except psycopg.errors.DuplicateColumn:
                print("A coluna 'aprovado' já existe. Nenhuma alteração necessária.")

def insert_pet(data):
    """
    Insere um novo registro na tabela 'cadastropet'.
    """
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO cadastropet (
                    nome, telefone, email, nomepet, statuspet, especiepet, 
                    racapet, corpet, localizacaopet, datapet, 
                    infoadicionalpet, imagempet
                )
                VALUES (%(nome)s, %(telefone)s, %(email)s, %(nomepet)s, %(statuspet)s, 
                        %(especiepet)s, %(racapet)s, %(corpet)s, %(localizacaopet)s, 
                        %(datapet)s, %(infoadicionalpet)s, %(imagempet)s)
            """, data)



from psycopg import connect

def fetch_approved_pets(status_pet):
    """
    Busca pets com um status específico ('Perdido' ou 'Encontrado') que foram aprovados.
    """
    # Consulta SQL
    query = """
        SELECT * FROM cadastropet 
        WHERE statuspet = %s AND aprovado = TRUE;
    """

    # String de conexão ao banco de dados no BigAnimal
    conn_string = "postgresql://edb_admin:Upandcoming92@p-r5xhpcs8oh.pg.biganimal.io:5432/petdatabase"

    try:
        # Conexão com o banco
        with connect(conn_string) as conn:
            with conn.cursor() as cur:
                # Executa a consulta com o parâmetro
                cur.execute(query, (status_pet,))
                rows = cur.fetchall()

                # Retorna os resultados como uma lista de dicionários
                return [
                    {
                        "nome": row[1],
                        "telefone": row[2],
                        "email": row[3],
                        "nomepet": row[4],
                        "statuspet": row[5],
                        "especiepet": row[6],
                        "racapet": row[7],
                        "corpet": row[8],
                        "localizacaopet": row[9],
                        "datapet": row[10],
                        "infoadicionalpet": row[11],
                        "imagempet": row[12],
                    }
                    for row in rows
                ]
    except Exception as e:
        raise RuntimeError(f"Erro ao buscar dados: {e}")


# def create_table():
#     with connect() as conn:
#         with conn.cursor() as cursor:
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS cadastropet (
#                     id SERIAL PRIMARY KEY,
#                     nome TEXT,
#                     telefone TEXT,
#                     email TEXT,
#                     nomepet TEXT,
#                     statuspet TEXT,
#                     especiepet TEXT,
#                     racapet TEXT,
#                     corpet TEXT,
#                     localizacaopet TEXT,
#                     datapet TEXT,
#                     infoadicionalpet TEXT,
#                     imagempet TEXT,
#                     aprovado INTEGER DEFAULT 0
#                 )
#             """)
#             conn.commit()

# def update_table_schema():
#     """
#     Adiciona a coluna 'aprovado' à tabela 'cadastropet', se ela não existir.
#     """
#     with connect() as conn:
#         with conn.cursor() as cursor:
#             # Tenta adicionar a coluna, ignorando o erro se ela já existir
#              try:
#                  cursor.execute("ALTER TABLE cadastropet ADD COLUMN aprovado INTEGER DEFAULT 0")
#              except psycopg.errors.DuplicateColumn:
#                  pass
#              conn.commit()



# def insert_pet(data):
#      with connect() as conn:
#          with conn.cursor() as cursor:
#              cursor.execute("""
#                  INSERT INTO cadastropet (nome, telefone, email, nomepet, statuspet, especiepet, racapet, corpet, localizacaopet, datapet, infoadicionalpet, imagempet)
#                  VALUES (%(nome)s, %(telefone)s, %(email)s, %(nomepet)s, %(statuspet)s, %(especiepet)s, %(racapet)s, %(corpet)s, %(localizacaopet)s, %(datapet)s, %(infoadicionalpet)s, %(imagempet)s)
#              """, data)
#              conn.commit()


# def fetch_approved_pets(status):
#      """
#      Retorna os pets aprovados com base no 'statuspet' (Perdido ou Encontrado).
#      """
#      with connect() as conn:
#          with conn.cursor() as cursor:
#              cursor.execute("""
#                  SELECT * FROM cadastropet
#                  WHERE statuspet = %s AND aprovado = 1
#              """, (status,))
            
#              # Verifique se o cursor tem uma descrição de colunas
#              if cursor.description is not None:
#                 columns = [col[0] for col in cursor.description]
#                 # Verifique se há resultados antes de tentar acessar
#                  if cursor.rowcount > 0:
#                     return [dict(zip(columns, row)) for row in cursor.fetchall()]
#                  else:
#                      return []  # Nenhum pet aprovado encontrado
#              else:
#                  return []  # Caso não tenha descrição de colunas


# def debug_database():
#      """
#      Lista todas as tabelas existentes no banco de dados.
#      """
#      with connect() as conn:
#          with conn.cursor() as cursor:
#              cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
#              tables = cursor.fetchall()
#              print(f"Tabelas no banco de dados: {tables}")

# def fetch_pending_pets(status):
#      """
#      Retorna os pets pendentes com base no 'statuspet' (Perdido ou Encontrado).
#      """
#      with connect() as conn:
#          with conn.cursor() as cursor:
#              cursor.execute("""
#                  SELECT * FROM cadastropet
#                  WHERE statuspet = %s AND aprovado = 0
#              """, (status,))
            
#              # Verifique se o cursor tem uma descrição de colunas
#              if cursor.description is not None:
#                  columns = [col[0] for col in cursor.description]
#                  # Verifique se há resultados antes de tentar acessar
#                  if cursor.rowcount > 0:
#                      return [dict(zip(columns, row)) for row in cursor.fetchall()]
#                  else:
#                      return []   #Nenhum pet encontrado
#              else:
#                  return []  # Caso não tenha descrição de colunas


# def approve_pet(pet_id):
#      with connect() as conn:
#          with conn.cursor() as cursor:
#              cursor.execute("UPDATE cadastropet SET aprovado = 1 WHERE id = %s", (pet_id,))
#              conn.commit()  # Certifique-se de que a transação seja salva

# # Função para rejeitar um pet (deletando o pet do banco de dados)
# def reject_pet(pet_id):
#      with connect() as conn:
#          with conn.cursor() as cursor:
#              cursor.execute("DELETE FROM cadastropet WHERE id = %s", (pet_id,))
#              conn.commit()  # Certifique-se de que a transação seja salva