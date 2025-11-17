# Importando bibliotecas
import socket, subprocess, platform, os

# Padronizando um tempo para resposta
socket.setdefaulttimeout(1)

# Entrada de Host com Menu
print("+", "-"*65, "+")
print("📌 Se certifique que o IP seja válido! De sua rede interna ou Público ")
print("+", "-"*65, "+")
host = input("Insira o IP> ")

# Teste se o Ip está em uso na rede antes de prosseguir
def testar_ip_ativo(ip):
    """
    Usa alguns métodos avançados como > dns reverso, tabela arp, o próprio ping etc
    """

    # Método 1: Conexão TCP em múltiplas portas (Mais acertivo que ping)
    portas_teste = [80, 443, 22, 23, 135, 445, 8080, 8443, 8081, 8291]

    # Percorre cada porta em busca de uma resposta
    for porta in portas_teste:
        try:
            s = socket.socket()
            resultado = s.connect_ex((ip, porta))
            s.close()

            if resultado == 0:
                print(f"✅  IP está ativo (responde na porta {porta})")
                return True
        except:
            continue

    # Método 2: Ping
    try:
        param = "-n" if platform.system().lower() == "windows" else "-c"
        comando = ["ping", param, "2", "-W", "1000", ip] #2 tentativas, timeout de 1s

        with open(os.devnull, "w") as devnull:
            resultado = subprocess.call(comando, stdout=devnull, stderr=devnull)

        if resultado == 0:
            print(f"✅ IP está ativo (responde ao ping)")
            return True
    except:
        pass

    # Método 3: DNS Reverso (Para Ips que possuem nome)
    try:
        nome_host = socket.gethostbyaddr(ip)
        print(f"✅ IP está ativo (resolução DNS: {nome_host[0]})")
        return True
    except:
        pass

    # Método 4: ARP (Para testes locais) - Verifica se o ip existe na tabela Arp
    try:
        if platform.system().lower() == "windows":
            comando = ["arp", "-a", ip]
        else:
            comando = ["arp", "-n", ip]

        resultado = subprocess.check_output(comando, universal_newlines=True)
        if ip in resultado and "incomplete" not in resultado:
            print(f"✅ IP está ativo (encontrado na tabela ARP)")
            return True
    except:
        pass

    # Caso nenhuma das opções sejam atendidas
    print("❌ IP não está ativo, ou não responde a nenhum teste!")
    print("\n💡 Possíveis causas:")
    print("   • O IP digitado está incorreto")
    print("   • O dispositivo está desligado")
    print("   • Você não está na mesma rede")
    print("   • Firewall está bloqueando a conexão")
    print("   • O host não existe")
    print(f"\n🚫 Programa encerrado! Verifique o IP {host} e tente novamente.")

    return False

# Criando a função para verificar as portas
def status_porta(porta):
    try:
        #Criando uma conexão
        s = socket.socket()

        # Testando comunicação
        resultado = s.connect_ex((host, porta))

        #Desliga conexão
        s.close()

        #Resposta
        return resultado ==0
    except:
        return False


# Lista de portas serviços conhecidos 
port_services = {
    20: "FTP (Data Transfer)",
    21: "FTP (Control)",
    22: "SSH (Secure Shell)",
    23: "Telnet",
    25: "SMTP (Simple Mail Transfer Protocol)",
    43: "WHOIS",
    53: "DNS (Domain Name System)",
    69: "TFTP (Trivial File Transfer Protocol)",
    80: "HTTP (Hypertext Transfer Protocol)",
    81: "HTTP Alternate",
    110: "POP3 (Post Office Protocol)",
    115: "SFTP (Simple File Transfer Protocol)",
    139: "SMB",
    156: "SQL Service",
    179: "BGP (Border Gateway Protocol)",
    443: "HTTPS (HTTP Secure)",
    445: "SMB",
    554: "RTSP (Real Time Streaming Protocol)",
    563: "NNTPS (NNTP over SSL)",
    587: "SMTP Submission (Email submission)",
    901: "Samba Web Administration Tool",
    904: "VMware Server",
    911: "Network Console on Acid",
    981: "SofaWare Technologies",
    989: "FTPS Protocol (data)",
    990: "FTPS Protocol (control)",
    1701: "L2TP (Layer 2 Tunneling Protocol)",
    1812: "RADIUS Authentication",
    1965: "Gemini Protocol",
    4899: "Radmin Remote Administration",
    5900: "VNC (Virtual Network Computing)",
    8080: "HTTP Alternate",
    8291: "Winbox - Mikrotik"
}

# Main
print(f"\n🎯 Verificando se {host} está ativo na rede...")

# Primeiro testa se o IP está ativo 
if testar_ip_ativo(host):
    # Se estiver ativo, faz o scan de portas
    print(f"\n🔍 Iniciando escaneamento de portas em {host}...")
    print("-" * 60)

    # Contadores
    portas_abertas = 0
    portas_fechadas = 0

    # Percorre a lista de portas
    for port, service in port_services.items():
        if status_porta(port):
            print(f"✅ Porta {port:4} - {service} aberta")
            portas_abertas+=1
        else: 
            print(f"❌ Porta {port:4} -{service} fechada")
            portas_fechadas +=1
    
    # Estatísticas finais
    print("-" * 60)
    print(f"📊 RELATÓRIO FINAL:")
    print(f"  ✅ Portas abertas: {portas_abertas}")
    print(f"  ❌ Portas fechadas: {portas_fechadas}")
    print(f"  📍 Total verificadas: {portas_abertas + portas_fechadas}")
    print(f"  🎯 Host: {host}")
