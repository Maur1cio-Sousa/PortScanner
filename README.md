# 🔍 PortScanner - Ferramenta de Análise de Portas em Python
Uma ferramenta de scanner de portas desenvolvida em Python para testes de segurança e auditoria de rede.
> ⚠️ **AVISO LEGAL**: Use esta ferramenta apenas em redes que você possui ou tem autorização explícita para testar. O uso não autorizado é ilegal.

## 🚀 Funcionalidades

### 🔎 Detecção Inteligente de Hosts
- **Multi-método de verificação**: ARP, ICMP, TCP, DNS reverso
- **Validação pré-scan**: Só escaneia hosts ativos
- **Suporte misto**: IPs (v4) e nomes de domínio
- **Timeout configurável**: Performance otimizada

### 📊 Scanner de Portas Avançado
- **30+ serviços mapeados**: Portas e serviços essenciais
- **Identificação automática**: Nome do serviço + número da porta
- **Relatório detalhado**: Estatísticas completas do scan
- **Interface clara**: Resultados coloridos e organizados

### 🛡️ Recursos de Segurança
- **Prevenção de scans desnecessários**
- **Configurações de timeout personalizáveis**
- **Tratamento robusto de exceções**
- **Logs de execução transparentes**

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/portscanner.git

# Acesse o diretório
cd PortScanner

# Execute o scanner
python portscanner.py
