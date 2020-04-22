#!/usr/bin/env python
import scapy.all as scapy
import optparse
def get_argument():
    parser=optparse.OptionParser()
    parser.add_option("-t","--target",dest="target",help="Entrt IP range to scan")
    options,argument=parser.parse_args()
    return options
def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    answerd_list=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    client_list=[]
    for element in answerd_list:
        client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(result_list):
    """

    :type result_list: object
    """
    print("IP\t\t\tMAC ADDRESS\n")
    for clients in result_list:
        print(clients["ip"]+"\t\t"+clients["mac"])

options=get_argument()
scan_result=scan(options.target)
print_result(scan_result)
