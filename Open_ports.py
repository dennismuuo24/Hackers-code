import psutil

def list_all_ports():
    connections = psutil.net_connections()
    ports_info = []

    for conn in connections:
        local_addr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        status = conn.status
        ports_info.append((local_addr, remote_addr, status))

    return ports_info

if __name__ == "__main__":
    ports_info = list_all_ports()
    if ports_info:
        print(f"{'Local Address':<30}{'Remote Address':<30}{'Status'}")
        print("="*70)
        for local_addr, remote_addr, status in ports_info:
            print(f"{local_addr:<30}{remote_addr:<30}{status}")
    else:
        print("No network connections found.")
