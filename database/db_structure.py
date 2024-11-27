from sqlalchemy import create_engine, text
import os

# URL de conexão com o banco
DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/petdatabase"

# Criar engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Testar conexão e executar consulta
with engine.connect() as connection:
    # Usar text para consultas SQL diretas
    stmt = text("SELECT 'Conexão bem-sucedida!' AS resultado")
    result = connection.execute(stmt)
    for row in result:
        # Acessar resultados corretamente
        print(row[0])  # Tente também row.resultado ou row[0] se der erro