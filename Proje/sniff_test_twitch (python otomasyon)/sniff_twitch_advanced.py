#!/usr/bin/env python3
import time
import ipaddress
import sys
from pathlib import Path
from scapy.all import sniff, IP, DNS, DNSQR, TCP, UDP, PcapWriter

# -----------------------------
# DOSYA YOLLARINI AYARLA (SCRIPTE GÖRE)
# -----------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
IP_FILE   = SCRIPT_DIR / "ips.txt"
PCAP_FILE = SCRIPT_DIR / "capture.pcap"
LOG_FILE  = SCRIPT_DIR / "sniff_log.txt"
TIMEOUT   = 120  # saniye

# -----------------------------
# IP BLOKLARINI YÜKLE (CIDR destekli, hatalı format toleranslı)
# -----------------------------
ip_networks = []

def load_ip_blocks():
    if not IP_FILE.exists():
        print(f"Hata: {IP_FILE} dosyası bulunamadı.")
        sys.exit(1)

    for line in IP_FILE.read_text(encoding='utf-8').splitlines():
        ip = line.strip().replace('\ufeff', '')  # BOM temizliği
        if not ip or ip.startswith("#"):
            continue
        try:
            net = ipaddress.ip_network(ip, strict=False)
            ip_networks.append(net)
        except ValueError:
            print(f"[!] Hatalı IP formatı atlandı: {ip!r}")

    if not ip_networks:
        print("Hata: Geçerli IP bloğu bulunamadı.")
        sys.exit(1)

    print(f"Yüklenen IP blok sayısı: {len(ip_networks)}")

# -----------------------------
# LOG DOSYASINA YAZ (UTF-8 KODLAMALI)
# -----------------------------
def write_log(text):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with LOG_FILE.open("a", encoding="utf-8") as log:
        log.write(f"{timestamp} - {text}\n")

# -----------------------------
# GÜVENLİ PRINT (Türkçe karakter sorunu için)
# -----------------------------
def safe_print(text):
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode("utf-8", errors="ignore").decode())

# -----------------------------
# IP EŞLEŞME FONKSİYONU
# -----------------------------
def ip_matches(ip_str):
    try:
        ip_obj = ipaddress.ip_address(ip_str)
        return any(ip_obj in net for net in ip_networks)
    except ValueError:
        return False

# -----------------------------
# PAKET CALLBACK (IP + DNS kontrolü)
# -----------------------------
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        matched = False
        match_reason = ""

        # 1) IP bloğu kontrolü
        if ip_matches(src_ip) or ip_matches(dst_ip):
            matched = True
            match_reason = "IP eşleşmesi"

        # 2) DNS sorgusunda twitch.tv kontrolü (hatalı paketlerde hata bastırılır)
        # Güvenli erişim ve sadece DNSQR olunca devam et!
        if packet.haslayer(DNS) and packet[DNS].qd is not None and packet.haslayer(DNSQR):
            try:
                qname_raw = packet[DNSQR].qname
                if isinstance(qname_raw, bytes):
                    qname = qname_raw.decode(errors="ignore").lower()
                    if "twitch.tv" in qname:
                        matched = True
                        match_reason = f'DNS sorgusu: "{qname}"'
            except Exception as e:
                safe_print(f"[!] DNS çözümleme hatası: {e}")

        if matched:
            proto = packet.sprintf("%IP.proto%")
            port = "N/A"
            if packet.haslayer(TCP):
                port = packet[TCP].dport
            elif packet.haslayer(UDP):
                port = packet[UDP].dport

            info = (f"Eşleşme: {src_ip} → {dst_ip} | Protokol: {proto} | "
                    f"Port: {port} | Sebep: {match_reason}")
            safe_print(info)
            write_log(info)
            pcap_writer.write(packet)

# -----------------------------
# ANA İŞLEM: SNIFF BAŞLAT
# -----------------------------
if __name__ == "__main__":
    safe_print("IP blokları yükleniyor...")
    load_ip_blocks()

    safe_print("Paket dinleme başlatılıyor... (Ctrl+C ile çıkabilir ya da 120 saniyede otomatik kapanır.)")
    pcap_writer = PcapWriter(str(PCAP_FILE), append=True, sync=True)

    start_time = time.time()
    def stop_filter(pkt):
        return (time.time() - start_time) > TIMEOUT

    try:
        sniff(prn=packet_callback,
              store=0,
              filter="tcp or udp",
              stop_filter=stop_filter)
    except KeyboardInterrupt:
        safe_print("\nSniffing manuel olarak durduruldu.")

    safe_print(f"Sniffing tamamlandı. Paketler kaydedildi: {PCAP_FILE.resolve()}")
    safe_print(f"Log dosyası: {LOG_FILE.resolve()}")
    input("\nKapatmak için ENTER'a basın...")
