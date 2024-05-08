import eel
from scapy.all import sniff, UDP, IP, Ether

eel.init('web')

packet_id = 0  # Initialize Packet ID
seen_ips = set()  # Track Seen IPs

@eel.expose
def start_sniffing():
    global packet_id, seen_ips

    def packet_callback(packet):
        global packet_id
        if UDP in packet and (packet[UDP].dport == 14235 or packet[UDP].dport == 8888):
            src_ip = packet[IP].src
            if src_ip not in seen_ips:
                seen_ips.add(src_ip)
                packet_id += 1
                data = {
                    'id': packet_id,
                    'ip_src': src_ip,
                    'mac_src': packet[Ether].src,
                    'port': packet[UDP].dport
                }
                eel.show_data(data)
                print(f"\033[92mNew IP detected: {src_ip} on Port: {packet[UDP].dport} with MAC: {packet[Ether].src} \033[0m")  # 92 is the ANSI code for green

    sniff(filter="udp and (port 14235 or port 8888)", prn=packet_callback, store=0)

eel.start('index.html', size=(800, 600))




















# from scapy.all import sniff, UDP, IP, Ether

# def packet_callback(packet):
#     if UDP in packet and (packet[UDP].dport == 14235 or packet[UDP].dport == 8888):
#         ip_src = packet[IP].src  # Source IP address
#         mac_src = packet[Ether].src  # Source MAC address
#         port = packet[UDP].dport  # Destination port
#         print(f"Received UDP from IP: {ip_src}, MAC: {mac_src}, Port: {port}")

# # Start sniffing with filter for UDP on port 14235 or 8888
# sniff(filter="udp and (port 14235 or port 8888)", prn=packet_callback, store=0)