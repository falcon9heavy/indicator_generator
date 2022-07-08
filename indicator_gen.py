# https://realpython.com/python-ipaddress-module/

from ipaddress import IPv4Network


def create_ips():
    list_ips = []
    net = IPv4Network('192.0.0.0/8')
    for addr in net:
        list_ips.append(addr)
    print(f' The number of IPs in this network is {len(list_ips)}')


def print_network_information(ipv4net: IPv4Network) -> None:
    """Prints the network address, broadcast address and number
    of addresses on the given IPv4 network.
    """

    print('Network IP:', ipv4net.network_address)
    print('Broadcast address:', ipv4net.broadcast_address)
    print('Number of hosts:', ipv4net.num_addresses)


def main() -> None:
    print_network_information(IPv4Network('192.0.0.0/8'))
    create_ips()


if __name__ == '__main__':
    main()
