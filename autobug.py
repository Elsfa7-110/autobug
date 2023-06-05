import subprocess
import time

def run_subfinder(domain):
    subfinder_command = f"subfinder -d {domain} -all -o subdomains.txt"
    subprocess.run(subfinder_command, shell=True)

def run_httprobe():
    httprobe_command = "cat subdomains.txt | httprobe -c 50 -t 3000 > httprobe.txt"
    subprocess.run(httprobe_command, shell=True)

def run_nuclei():
    nuclei_command = f"nuclei -l httprobe.txt -t ~/nuclei-templates/ -o nuclei_output.txt"
    subprocess.run(nuclei_command, shell=True)

if __name__ == '__main__':
    while True:
        domain = input("Enter a domain to scan: ")
        run_subfinder(domain)
        run_httprobe()
        run_nuclei()
        time.sleep(3600)  # wait for 1 hour
