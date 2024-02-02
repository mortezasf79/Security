import socket
import os

def scan_ip_range(start_ip, end_ip):
    active_hosts = []

    try:
        start_ip_split = start_ip.split('.')
        end_ip_split = end_ip.split('.')


        start_ip_int = int(start_ip_split[3])
        end_ip_int = int(end_ip_split[3])

        for i in range(start_ip_int, end_ip_int + 1):
            ip = f"{start_ip_split[0]}.{start_ip_split[1]}.{start_ip_split[2]}.{i}"
            response = os.system(f"ping -n 1 -w 1000 {ip}")
            print(response)

            if response == 0:
                active_hosts.append(ip)
        
        print(active_hosts)

        return active_hosts

    except Exception as e:
        print(f"Error in scan ip range: {str(e)}")
        return active_hosts




def scan_ports(ip_address, start_port, end_port, protocol):
    open_ports = []

    try:
        for port in range(start_port, end_port + 1):
            if protocol == 'tcp':
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))

            if result == 0:
                open_ports.append(port)

            sock.close()

        return open_ports

    except Exception as e:
        print(f"Error in port scan: {str(e)}")
        return open_ports

def save_report(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"report {filename} saved succussfuly.")

    except Exception as e:
        print(f"Error in save report. {str(e)}")





def identify_service(ip, port):
    try:
        service_name = socket.getservbyport(port)
        return service_name

    except Exception as e:
        print(f"Error identifying the service on the port: {port}: {str(e)}")
        return None

def main():
    import argparse
    parser = argparse.ArgumentParser(description='اسکن محدوده آی‌پی و یافتن ماشین‌های فعال یا اسکن پورت‌ها')
    parser.add_argument('--ipscan', action='store_true', help='اسکن محدوده آی‌پی')
    parser.add_argument('-m', '--subnet_mask', type=int, help='ماسک زیرشبکه')
    parser.add_argument('-ip', '--ip_range', nargs='+', help='محدوده آی‌پی (شروع و پایان)')
    parser.add_argument('-p', '--portscan', action='store_true', help='اسکن پورت‌ها')
    parser.add_argument('-t', '--tcp', action='store_true', help='اسکن پورت‌های TCP')
    parser.add_argument('-u', '--udp', action='store_true', help='اسکن پورت‌های UDP')
    parser.add_argument('ip', type=str, nargs='?', help='اسکن آی‌پی')
    parser.add_argument('start_port', type=int, nargs='?', help='پورت شروع')
    parser.add_argument('end_port', type=int, nargs='?', help='پورت پایان')

    args = parser.parse_args()

    if args.ipscan:
        if args.subnet_mask and args.ip_range:
            start_ip = args.ip_range[0]
            end_ip = args.ip_range[1]
            subnet_mask = args.subnet_mask

            active_hosts = scan_ip_range(start_ip, end_ip)
            
            report_content = ""

            for host in active_hosts:
                report_content += f"Ip address {host}\n"

            save_report("report.txt", report_content)
        else:
            print('Please specify the IP range and subnet mask')

    elif args.portscan:
        if args.tcp:
            protocol = 'tcp'
        elif args.udp:
            protocol = 'udp'
        else:
            print('To scan ports, you must choose one of TCP and UDP protocols.')
            return

        open_ports = scan_ports(args.ip, args.start_port, args.end_port, protocol)
        if len(open_ports) > 0:
            report_content = f"Open ports {protocol.upper()}:\n"
            for port in open_ports:
                report_content += f"port - {port}:\n"
                report_content += f"Service - {identify_service(args.ip, port)}\n\n"
        else:
            report_content = f"open port {protocol.upper()} not found"

        save_report("report.txt", report_content)



    

if __name__ == "__main__":
    main()