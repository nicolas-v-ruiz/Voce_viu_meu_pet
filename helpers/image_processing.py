from pathlib import Path
from PIL import Image
import re
# Configura o diretório absoluto para uploads
UPLOADS_DIR = Path("C:/Users/FN84/OneDrive - PETROBRAS/Área de Trabalho/VoceViumeuPet - CRUD/projeto/uploads")
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)  # Garante que o diretório existe
def process_image(image_file, metadata, max_size=(800, 800)):
    """
    Processa e salva a imagem no diretório absoluto 'UPLOADS_DIR'.
    """
    from PIL import Image
    import uuid
    if image_file is None or not hasattr(image_file, "read"):
        raise ValueError("Nenhuma imagem válida foi carregada.")
    if 'nomepet' not in metadata or 'datapet' not in metadata:
        raise ValueError("Metadados obrigatórios ausentes ('nomepet' ou 'datapet').")
    try:
        # Validar o formato da imagem
        validate_image_format(image_file)
        # Gerar um identificador único para a imagem
        image_id = str(uuid.uuid4())  # Exemplo: '123e4567-e89b-12d3-a456-426614174000'
        file_name = f"{image_id}.png"  # Nome do arquivo com extensão
        # Caminho completo no sistema de arquivos
        file_path = UPLOADS_DIR / file_name
        # Abrir, redimensionar e salvar a imagem
        image = Image.open(image_file)
        image = resize_image(image, max_size)
        image.save(file_path, format="PNG", optimize=True, quality=85)
        # Retornar apenas o nome do arquivo (para salvar no banco)
        return file_name
    except (OSError, ValueError, IOError) as e:
        raise RuntimeError(f"Erro ao processar a imagem: {e}")
# def process_image(image_file, metadata, upload_dir="uploads", max_size=(800, 800)):
    if image_file is None or not hasattr(image_file, "read"):
        raise ValueError("Nenhuma imagem válida foi carregada.")
    if 'nomepet' not in metadata or 'datapet' not in metadata:
        raise ValueError("Metadados obrigatórios ausentes ('nomepet' ou 'datapet').")
    try:
        # Validar o formato da imagem
        validate_image_format(image_file)
        # Criar diretório base para salvar a imagem
        upload_path = Path(upload_dir)
        upload_path.mkdir(parents=True, exist_ok=True)
        # Gerar um identificador único para a imagem
        image_id = str(uuid.uuid4())  # Exemplo: '123e4567-e89b-12d3-a456-426614174000'
        file_name = f"{image_id}.png"  # Salva com o ID no nome do arquivo
        # Caminho completo no sistema de arquivos
        file_path = upload_path / file_name
        # Abrir, redimensionar e salvar a imagem
        image = Image.open(image_file)
        image = resize_image(image, max_size)
        image.save(file_path, format="PNG", optimize=True, quality=85)
        # Retornar apenas o identificador único
        return image_id
    except (OSError, ValueError, IOError) as e:
        raise RuntimeError(f"Erro ao processar a imagem: {e}")
def validate_image_format(image_file):
    valid_formats = ["JPEG", "PNG"]
    try:
        image_format = Image.open(image_file).format
        if image_format not in valid_formats:
            raise ValueError("Formato de arquivo inválido. Use JPEG ou PNG.")
    except Exception as e:
        raise ValueError(f"Erro ao validar formato da imagem: {e}")
    return True
def sanitize_filename(filename, max_length=255):
    sanitized = re.sub(r"[^a-zA-Z0-9_-]", "", filename.strip())
    if not sanitized:
        raise ValueError("Nome de arquivo inválido após sanitização.")
    return sanitized[:max_length]
def resize_image(image, max_size=(800, 800)):
    image.thumbnail(max_size)
    return image