import socket
import argparse
import time
import concurrent.futures
from typing import List, Tuple

def parse_ports(ports_str: str) -> List[int]:
    """Converte uma string de portas (ex.: '80,443,20-100') em uma lista de números."""
    ports = []
    try:
        for part in ports_str.replace(" ", "").split(","):
            if "-" in part:
                start, end = map(int, part.split("-"))
                if not (1 <= start <= 65535 and 1 <= end <= 65535):
                    raise ValueError("Portas devem estar entre 1 e 65535.")
                ports.extend(range(start, end + 1))
            else:
                port = int(part)
                if not (1 <= port <= 65535):
                    raise ValueError("Portas devem estar entre 1 e 65535.")
                ports.append(port)
        return sorted(list(set(ports)))  # Remove duplicatas e ordena
    except ValueError as e:
        raise ValueError(f"Erro ao processar portas: {e}")

def scan_port(host: str, port: int, timeout: float) -> Tuple[int, str]:
    """Escaneia uma única porta e retorna seu status."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            return port, "ABERTA"
        else:
            return port, "FECHADA"
    except socket.timeout:
        return port, "FILTRADA"
    except socket.gaierror:
        raise ValueError(f"Não foi possível resolver o host: {host}")
    except socket.error:
        return port, "ERRO"
    finally:
        sock.close()

def scan_ports(host: str, ports: List[int], timeout: float) -> List[Tuple[int, str]]:
    """Escaneia múltiplas portas em paralelo usando ThreadPoolExecutor."""
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_port = {executor.submit(scan_port, host, port, timeout): port for port in ports}
        for future in concurrent.futures.as_completed(future_to_port):
            results.append(future.result())
    return sorted(results, key=lambda x: x[0])  # Ordena por número da porta

def main():
    """Função principal para configurar e executar o scanner de portas."""
    parser = argparse.ArgumentParser(description="Port Scanner - Verifica portas abertas em um host.")
    parser.add_argument("host", help="IP ou hostname a ser escaneado (ex.: localhost, 192.168.1.1)")
    parser.add_argument("-p", "--ports", required=True, help="Portas a escanear (ex.: 80, 80,443, 20-100)")
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Timeout por porta em segundos (padrão: 1)")
    args = parser.parse_args()

    print(f"Escaneando {args.host}...")
    start_time = time.time()

    try:
        # Resolve o hostname para IP
        ip = socket.gethostbyname(args.host)
        print(f"IP resolvido: {ip}")

        # Processa as portas
        ports = parse_ports(args.ports)

        # Executa o escaneamento
        results = scan_ports(ip, ports, args.timeout)

        # Exibe os resultados
        for port, status in results:
            print(f"Porta {port}: {status}")

        print(f"Escaneamento concluído em {time.time() - start_time:.2f} segundos.")

    except ValueError as e:
        print(f"Erro: {e}")
    except KeyboardInterrupt:
        print("\nEscaneamento interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()