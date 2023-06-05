import subprocess
import time

def run_subdomain_scanners(domain):
    subfinder_command = f"subfinder -d {domain} -o subdomains.txt"
    findomain_command = f"findomain -t {domain} -u subdomains.txt"
    subprocess.run(subfinder_command, shell=True)
    subprocess.run(findomain_command, shell=True)

def remove_duplicates():
    sort_command = "sort subdomains.txt | uniq > subdomains_sorted.txt"
    mv_command = "mv subdomains_sorted.txt subdomains.txt"
    subprocess.run(sort_command, shell=True)
    subprocess.run(mv_command, shell=True)

def run_httprobe():
    httprobe_command = "cat subdomains.txt | httprobe -c 50 -t 3000 > httprobe.txt"
    subprocess.run(httprobe_command, shell=True)

def run_nuclei():
    nuclei_command = f"nuclei -l httprobe.txt -t ~/nuclei-templates/ -o nuclei_output.txt"
    subprocess.run(nuclei_command, shell=True)

if __name__ == '__main__':
    while True:
        domain = input("Enter a domain to scan: ")
        run_subdomain_scanners(domain)
        remove_duplicates()
        run_httprobe()
        run_nuclei()
        time.sleep(3600)  # wait for 1 hour
