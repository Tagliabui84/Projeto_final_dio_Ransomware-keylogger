# decryptor.py
from ransomware_sim import RansomwareSimulado

def main():
    print("="*60)
    print("🔓 DECRIPTADOR DE ARQUIVOS - RESTAURAÇÃO 🔓")
    print("="*60)
    
    pasta = input("Digite o caminho da pasta a restaurar (ou Enter para 'arquivos_teste'): ").strip()
    if not pasta:
        pasta = "arquivos_teste"
    
    ransomware = RansomwareSimulado(pasta_alvo=pasta)
    
    try:
        ransomware.descriptografar()
    except Exception as e:
        print(f"\n❌ Erro ao descriptografar: {e}")
        print("Certifique-se de que o arquivo 'chave_secreta.key' existe no diretório atual.")

if __name__ == "__main__":
    main()