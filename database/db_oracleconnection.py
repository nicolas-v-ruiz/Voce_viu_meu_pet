# import oracledb
# import os

# # Configuração do Wallet
# os.environ['TNS_ADMIN'] = r'C:/Users/FN84/wallet_oracle'

# # Configurar DSN diretamente
# dsn = "(description=(retry_count=20)(retry_delay=3)" \
#       "(address=(protocol=tcps)(port=1522)(host=g7ada16f6dc1ad3-petdatabase_high.adb.oraclecloud.com))" \
#       "(connect_data=(service_name=g7ada16f6dc1ad3_petdatabase_high.adb.oraclecloud.com))" \
#       "(security=(ssl_server_dn_match=yes)))"

# # Testar conexão
# try:
#     connection = oracledb.connect(
#         user="ADMIN",
#         password="Marilia@1992",
#         dsn=dsn
#     )
#     print("Conexão bem-sucedida!")
# except oracledb.DatabaseError as e:
#     print("Erro ao conectar:", e)
