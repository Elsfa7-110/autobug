# autobug
automated get subdomains every hour and scan it by nuclei

This tool will get the subdomains for any domain by using subfinder and findomain and remove duplicates then result will go to httprobe and scan all result by nuclei

The script will repeat the same action every hour

to run it

python autobug.py
