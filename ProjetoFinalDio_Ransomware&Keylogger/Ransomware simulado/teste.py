# criar_arquivos_teste.py
import os

def criar_arquivos_teste():
    """Cria arquivos de teste para o ransomware"""
    os.makedirs("arquivos_teste", exist_ok=True)
    
    arquivos = {
        "documento.txt": "Conteúdo importante do meu trabalho...",
        "dados_pessoais.txt": "Nome: João, Email: joao@email.com",
        "backup_importante.txt": "Dados de backup do sistema...",
        "foto_perfil.jpg.txt": "Descrição da imagem..."
    }
    
    for nome, conteudo in arquivos.items():
        caminho = os.path.join("arquivos_teste", nome)
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"✅ Criado: {nome}")
    
    return list(arquivos.keys())

if __name__ == "__main__":
    criar_arquivos_teste()