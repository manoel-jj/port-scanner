Port Scanner - Projeto de Cibersegurança
Sobre o Projeto
O Port Scanner é uma ferramenta desenvolvida em Python para escanear portas de um endereço IP ou hostname, verificando se estão abertas, fechadas ou filtradas. Este projeto foi criado como parte do meu portfólio de cibersegurança, demonstrando conhecimentos em redes, programação Python e desenvolvimento de ferramentas de segurança.
O objetivo é educativo: entender conceitos de redes, como portas, sockets e comunicação TCP, enquanto aplico boas práticas de programação, como modularidade, tratamento de erros e interface de linha de comando.
Funcionalidades

Escaneia portas específicas (ex.: 80, 443) ou intervalos (ex.: 20-100).
Suporta IPs e hostnames (ex.: localhost, example.com).
Exibe status detalhado de cada porta (aberta, fechada, filtrada).
Interface via linha de comando com argumentos configuráveis.
Escaneamento paralelo para maior eficiência.
Configuração de timeout para otimizar a velocidade.

Tecnologias Utilizadas

Python: Linguagem principal.
Biblioteca socket: Para conexões TCP.
Biblioteca argparse: Para parsing de argumentos.
Biblioteca concurrent.futures: Para escaneamento multithread.

Como Usar
Pré-requisitos

Python 3.6 ou superior.
Permissões de rede (portas abaixo de 1024 podem exigir privilégios de administrador).

Instalação

Clone esse repositório


Verifique se o Python está instalado:python3 --version



Executando o Scanner
O script (port_scanner.py) é executado via linha de comando. Exemplos:
# Escanear portas comuns no localhost
python3 port_scanner.py localhost -p 22,80,443

# Escanear um intervalo de portas
python3 port_scanner.py 192.168.1.1 -p 20-100

# Escanear com timeout maior
python3 port_scanner.py example.com -p 80,443 -t 2

Argumentos

host: IP ou hostname (ex.: localhost, 192.168.1.1).
-p, --ports: Portas a escanear (ex.: 80, 80,443, 20-100).
-t, --timeout: Tempo de espera por conexão, em segundos (padrão: 1).

Exemplo de Saída
Escaneando localhost (127.0.0.1)...
Porta 22: ABERTA
Porta 80: FECHADA
Porta 443: FILTRADA
Escaneamento concluído em 2.34 segundos.

Ética e Uso Responsável

Aviso: Esta ferramenta é para fins educacionais. Escaneie apenas redes ou sistemas com autorização explícita. Escaneamentos não autorizados podem ser ilegais.
Limitações: O scanner usa conexões TCP completas e não suporta UDP ou técnicas avançadas como SYN scanning.

Estrutura do Código
O script port_scanner.py é modular e bem comentado:

parse_ports(): Processa a string de portas em uma lista.
scan_port(): Verifica o status de uma porta.
scan_ports(): Gerencia o escaneamento paralelo.
main(): Configura argumentos e exibe resultados.

Por que este Projeto?
Este projeto destaca minhas competências em:

Redes: Compreensão de portas, protocolos TCP e sockets.
Programação: Código modular, com tratamento de erros e interface amigável.
Cibersegurança: Desenvolvimento de ferramentas de pentest com ética.
Documentação: Comunicação clara de conceitos técnicos.



Como Contribuir:
Sinta-se à vontade para abrir issues ou pull requests com sugestões ou melhorias!
Contato



LinkedIn: https://www.linkedin.com/in/manoel-jj


Nota: Este projeto reflete meu compromisso com o aprendizado contínuo e o uso ético de ferramentas de cibersegurança.
