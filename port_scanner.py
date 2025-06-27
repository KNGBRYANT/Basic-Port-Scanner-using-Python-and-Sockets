import socket

def scan_ports(target, ports):
    print(f"\nScanning {target}...\n")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            s.close()
        except socket.error:
            print(f"Error scanning port {port}")
            continue

# Common ports to scan
common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3306]

target_ip = input("Enter IP address or domain to scan: ")
scan_ports(target_ip, common_ports)
