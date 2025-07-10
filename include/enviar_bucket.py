import boto3
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da AWS a partir do .env
AWS_ACCESS_KEY_ID: str = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY: str = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION: str = os.getenv('AWS_REGION')
BUCKET_NAME: str = os.getenv('BUCKET_NAME')

# Print para verificar se as variáveis de ambiente foram carregadas corretamente
print(f"AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID}")
print(f"AWS_SECRET_ACCESS_KEY: {AWS_SECRET_ACCESS_KEY}")
print(f"AWS_REGION: {AWS_REGION}")
print(f"BUCKET_NAME: {BUCKET_NAME}")

# Instanciar client s3
class EnviarParaBucket():
    def instanciar_bucket(self):
        try:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                region_name=AWS_REGION
            )
            print("Cliente S3 configurado com sucesso.")
        except Exception as e:
            raise Exception("Não foi possível inicializar o cliente.")

    # Ler Arquivos
    def ler_arquivos(self, pasta):
        try:
            arquivos = []
            for arquivo in os.listdir(pasta):
                caminho_completo = os.path.join(pasta, arquivo)
                if os.path.isfile(caminho_completo):
                    arquivos.append(caminho_completo)
            print("Arquivos lidos com sucesso.")
        except Exception as e:
            raise
        return arquivos

    # Upload arquivos para bucket
    def upload_arquivos(self, arquivos):
        try:
            for arquivo in arquivos:
                nome_arquivo = os.path.basename(arquivo)
                self.s3_client.upload_file(arquivo, BUCKET_NAME, nome_arquivo)
                print(f"Arquivo {nome_arquivo}, upado para o bucket")
        except Exception as e:
            raise Exception(f"Não foi possível realizar o upload do arquivo {arquivo} no bucket {BUCKET_NAME}: {e}")
            

    # Pipeline
    def executar_backup(self):
        try:
            arquivos = self.ler_arquivos('../data/')
            if arquivos:
                self.upload_arquivos(arquivos)
            else:
                print("Nenhum arquivo encontrado.")
        except Exception as e:
            raise Exception("Erro ao processar realizar o backup dos arquivos para o S3: {e}")