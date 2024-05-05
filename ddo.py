import subprocess
import time

def ping_ip(ip):
    try:
        subprocess.run(["ping", "-c", "1", ip], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Ping to {ip} successful.")
    except subprocess.CalledProcessError:
        print(f"Ping to {ip} failed.")

def main():
    ip = "192.168.0.1"
    num_pings = 50000
    interval = 0.02  # ثانية واحدة / 50 ألف = 0.02 ثانية

    for _ in range(num_pings):
        ping_ip(ip)
        time.sleep(interval)

if __name__ == "__main__":
    main()