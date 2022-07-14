# https://realpython.com/python-ipaddress-module/
# https://www.geeksforgeeks.org/with-statement-in-python/

from ipaddress import IPv4Network
import csv
import string
import random

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

def get_ips() -> list:
    list_ips = []
    net = IPv4Network('192.168.1.0/26')
    for addr in net:
        list_ips.append(addr)
    return list_ips
    #print(f' The number of IPs in this network is {len(list_ips)}')


def print_network_information(ipv4net: IPv4Network) -> None:
    """Prints the network address, broadcast address and number
    of addresses on the given IPv4 network.
    """
    print('Network IP:', ipv4net.network_address)
    print('Broadcast address:', ipv4net.broadcast_address)
    print('Number of hosts:', ipv4net.num_addresses)

def main() -> None:
    # nice part is that WITH handles resource mgmt
    net = IPv4Network('192.168.0.0/16')
    with open('ip_addresses.csv', 'w') as f:
        writer = csv.writer(f)
        for value in net:
            writer.writerow([value])


if __name__ == '__main__':
    main()
