# Create the python script
nano packet_sniffer.py

# python script
import socket
import struct

def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('!6s6sH', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

def ipv4_packet(data):
    version_header_length = data[0]
    header_length = (version_header_length & 15) * 4
    src = socket.inet_ntoa(data[12:16])
    target = socket.inet_ntoa(data[16:20])
    return src, target, data[header_length:]

def main():
    # Replace 'wlan0' with your real interface (eth0, wlan0, etc)
    interface = 'wlan0'
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    conn.bind((interface, 0))

    try:
        while True:
            raw_data, addr = conn.recvfrom(65535)
            dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
            print('\nEthernet Frame:')
            print(f'Destination MAC: {dest_mac}, Source MAC: {src_mac}, Protocol: {eth_proto}')
            
            if eth_proto == 8:  # IPv4
                src_ip, dest_ip, payload = ipv4_packet(data)
                print(f'IPv4 Packet:')
                print(f'Source IP: {src_ip}, Destination IP: {dest_ip}')
                print(f'Payload (first 100 bytes): {payload[:100]}')
    except KeyboardInterrupt:
        print("\n[+] CTRL+C detected. Exiting the sniffer...")
        conn.close()

if __name__ == "__main__":
    main()

# Make the script executable
chmod +x packet_sniffer.py

# Run
sudo python3 packet_sniffer.py

