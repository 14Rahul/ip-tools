#!/usr/bin/env python3
import argparse
import ipaddress
import psutil
import socket
import sys

def get_ip_networks():
    
    #Scans the network interfaces of the container and returns a list of configured IPv4 networks in CIDR notation.
    
    networks = []
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ip = addr.address
                netmask = addr.netmask
                try:
                    # Create an IPv4Interface to automatically calculate the network.
                    interface_network = ipaddress.IPv4Interface(f"{ip}/{netmask}").network
                    networks.append(str(interface_network))
                except Exception as e:
                    print(f"Error processing {ip}/{netmask} on {interface}: {e}", file=sys.stderr)
    # Remove duplicates (if any)
    return list(set(networks))

def check_collision(file_path):
    # Reads a file of IP networks (one per line) and checks if any networks overlap. Prints out any collisions.
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    networks = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            # strict=False allows non-canonical networks (e.g. 192.168.1.5/24)
            net = ipaddress.ip_network(line, strict=False)
            networks.append(net)
        except ValueError as e:
            print(f"Invalid network '{line}': {e}", file=sys.stderr)
    
    collisions = []
    for i in range(len(networks)):
        for j in range(i + 1, len(networks)):
            if networks[i].overlaps(networks[j]):
                collisions.append((str(networks[i]), str(networks[j])))
    
    if collisions:
        print("Colliding IP networks found:")
        for net1, net2 in collisions:
            print(f"  {net1} collides with {net2}")
    else:
        print("No collisions found.")

def main():
    parser = argparse.ArgumentParser(
        description="IP Tool for exploring IP range collisions in a Kubernetes cluster."
    )
    parser.add_argument("--check-collision", type=str,
                        help="Path to file containing concatenated list of IP networks from the cluster")
    args = parser.parse_args()

    if args.check_collision:
        check_collision(args.check_collision)
    else:
        networks = get_ip_networks()
        print("Configured IP networks in this container:")
        for net in networks:
            print(f"  {net}")

if __name__ == "__main__":
    main()
