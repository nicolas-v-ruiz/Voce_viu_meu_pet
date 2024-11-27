from sqlalchemy import create_engine, text
import os

# Configuração do Wallet
os.environ['TNS_ADMIN'] = r'C:/Users/FN84/wallet_oracle'  # Substitua pelo caminho correto

# URL de conexão com o banco
DATABASE_URL = "oracle+oracledb://ADMIN:Marilia%401992@g7ada16f6dc1ad3_petdatabase_high.adb.oraclecloud.com"

# Criar engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Testar conexão e executar consulta
with engine.connect() as connection:
    # Usar text para consultas SQL diretas
    stmt = text("SELECT 'Conexão bem-sucedida!' AS resultado FROM dual")
    result = connection.execute(stmt)
    for row in result:
        # Acessar resultados corretamente
        print(row[0])  # Tente também row.resultado ou row[0] se der erro
