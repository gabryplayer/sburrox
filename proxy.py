import re
import random
import socket
import struct
from colorama import Fore, Style, init
import time
import concurrent.futures
import requests
import subprocess



print("This Tool Gen Infinite Only Working Proxyes.")
print("Wait Two Second For Start...")

time.sleep(2)

# Create a session for proxy requests
proxy_session = requests.Session()

def generate_proxy_list():
    response = proxy_session.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all')
    if response.status_code == 200:
        proxy_list = response.text.split('\r\n')
        return proxy_list
    else:
        return []

def check_proxy(proxy):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = proxy_session.get('https://www.example.com', proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(Fore.GREEN + f'Proxy {proxy} is working' + Style.RESET_ALL)
            # Create a new "working_proxies.txt" file and save the working proxy
            with open('working_proxies.txt', 'a') as file:
                file.write(proxy + '\n')
    except requests.RequestException:
        pass  # Do nothing if the proxy is not working

# Adjust the number of concurrent threads for faster checking (e.g., 20 threads)
max_threads = 500000

# Loop to continuously fetch and check proxies
while True:
    # Generate a list of proxies
    proxy_list = generate_proxy_list()

    # Use concurrent.futures for parallel execution with max_threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(check_proxy, proxy_list)
