import psycopg2
import os

def connect():
    # Conectar ao banco de dados PostgreSQL
    conn = psycopg2.connect(
        dbname="petdatabase",
        user="username",
        password="password",
        host="localhost",
        port="5432"
    )
    return conn

def create_table():
    with connect() as conn:
        cursor = conn.cursor()
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
                datapet TEXT,
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
        cursor = conn.cursor()
        # Tenta adicionar a coluna, ignorando o erro se ela já existir
        try:
            cursor.execute("ALTER TABLE cadastropet ADD COLUMN aprovado INTEGER DEFAULT 0")
        except psycopg2.errors.DuplicateColumn:
            pass
        conn.commit()

def insert_pet(data):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cadastropet (nome, telefone, email, nomepet, statuspet, especiepet, racapet, corpet, localizacaopet, datapet, infoadicionalpet, imagempet)
            VALUES (%(nome)s, %(telefone)s, %(email)s, %(nomepet)s, %(statuspet)s, %(especiepet)s, %(racapet)s, %(corpet)s, %(localizacaopet)s, %(datapet)s, %(infoadicionalpet)s, %(imagempet)s)
        """, data)
        conn.commit()

def fetch_approved_pets(status):
    """
    Retorna os pets aprovados com base no 'statuspet' (Perdido ou Encontrado).
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM cadastropet
            WHERE statuspet = %s AND aprovado = 1
        """, (status,))
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

def debug_database():
    """
    Lista todas as tabelas existentes no banco de dados.
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tables = cursor.fetchall()
        print(f"Tabelas no banco de dados: {tables}")

def fetch_pending_pets(status):
    """
    Retorna os pets pendentes com base no 'statuspet' (Perdido ou Encontrado).
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM cadastropet
            WHERE statuspet = %s AND aprovado = 0
        """, (status,))
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

def approve_pet(pet_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE cadastropet SET aprovado = 1 WHERE id = %s", (pet_id,))
        conn.commit()  # Certifique-se de que a transação seja salva

# Função para rejeitar um pet (deletando o pet do banco de dados)
def reject_pet(pet_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cadastropet WHERE id = %s", (pet_id,))
        conn.commit()  # Certifique-se de que a transação seja salva