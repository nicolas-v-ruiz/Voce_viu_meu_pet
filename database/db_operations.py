import sqlite3
import os

def connect():
    # Caminho absoluto para o banco de dados na raiz do projeto
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../pet_database.db"))
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Banco de dados não encontrado no caminho: {db_path}")
    return sqlite3.connect(db_path)

def create_table():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cadastropet (
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
                imagempet TEXT)
        """)

def update_table_schema():
    """
    Adiciona a coluna 'aprovado' à tabela 'cadastropet', se ela não existir.
    """
    with connect() as conn:
        cursor = conn.cursor()
        # Tenta adicionar a coluna, ignorando o erro se ela já existir
        try:
            cursor.execute("ALTER TABLE cadastropet ADD COLUMN aprovado INTEGER DEFAULT 0")
        except sqlite3.OperationalError as e:
            # Caso a coluna já exista, o erro será ignorado
            if "duplicate column name: aprovado" not in str(e).lower():
                raise e

def insert_pet(data):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cadastropet (nome, telefone, email, nomepet, statuspet, especiepet, racapet, corpet, localizacaopet, datapet, infoadicionalpet, imagempet)
            VALUES (:nome, :telefone, :email, :nomepet, :statuspet, :especiepet, :racapet, :corpet, :localizacaopet, :datapet, :infoadicionalpet, :imagempet)
        """, data)

def fetch_approved_pets(status):
    """
    Retorna os pets aprovados com base no 'statuspet' (Perdido ou Encontrado).
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM cadastropet
            WHERE statuspet = ? AND aprovado = 1
        """, (status,))
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
def debug_database():
    """
    Lista todas as tabelas existentes no banco de dados.
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print(f"Tabelas no banco de dados: {tables}")
def approve_pet(pet_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE cadastropet SET aprovado = 1 WHERE rowid = ?", (pet_id,))
def reject_pet(pet_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cadastropet WHERE rowid = ?", (pet_id,))