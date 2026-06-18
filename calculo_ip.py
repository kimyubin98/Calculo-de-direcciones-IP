import ipaddress

def subnet_info(network):
    net = ipaddress.ip_network(network, strict=False)

    print("\n========== SUBNET INFO ==========")
    print(f"Network:        {net.network_address}")
    print(f"Subnet Mask:    {net.netmask}")
    print(f"Wildcard Mask:  {ipaddress.IPv4Address(int(net.hostmask))}")
    print(f"Broadcast:      {net.broadcast_address}")

    hosts = list(net.hosts())
    if len(hosts) >= 2:
        print(f"First Host:     {hosts[0]}")
        print(f"Last Host:      {hosts[-1]}")
    elif len(hosts) == 1:
        print(f"Only Host:      {hosts[0]}")
    else:
        print("No usable hosts")

    print(f"Total Hosts:    {net.num_addresses}")
    usable = max(0, net.num_addresses - (2 if net.prefixlen < 31 else 0))
    print(f"Usable Hosts:   {usable}")
    print("=================================\n")


def vlsm(base_network, host_requirements):
    base = ipaddress.ip_network(base_network, strict=False)

    # Sort hosts biggest → smallest
    host_requirements.sort(reverse=True)

    subnets = []
    current_ip = int(base.network_address)

    print("\n========== VLSM PLAN ==========")
    for hosts in host_requirements:
        needed = hosts + 2  # network + broadcast
        prefix = 32

        while (2 ** (32 - prefix)) < needed:
            prefix -= 1

        candidate = ipaddress.ip_network(
            f"{ipaddress.IPv4Address(current_ip)}/{prefix}",
            strict=False
        )
        if int(candidate.network_address) < current_ip:
            candidate = ipaddress.ip_network(
                f"{ipaddress.IPv4Address(int(candidate.network_address) + (1 << (32 - prefix)))}/{prefix}",
                strict=False
            )

        if candidate.broadcast_address > base.broadcast_address:
            print(f" No hay espacio para {hosts} hosts")
            continue

        subnets.append((hosts, candidate))
        current_ip = int(candidate.broadcast_address) + 1

    total_used = 0
    for hosts, net in subnets:
        usable = max(0, net.num_addresses - 2)
        total_used += usable
        print(f"\nSubnet for {hosts} hosts")
        print(f"Network:      {net.network_address}")
        print(f"Mask:         {net.netmask}")
        print(f"Prefix:       /{net.prefixlen}")
        print(f"Broadcast:    {net.broadcast_address}")
        print(f"Usable Hosts: {usable}")
        print(f"Range:        {list(net.hosts())[0]} - {list(net.hosts())[-1]}")

    print("\n========== SUMMARY ==========")
    print(f"Base Network:  {base}")
    print(f"Total space:   {base.num_addresses}")
    print(f"Total usable:  {max(0, base.num_addresses - 2)}")
    print(f"Used usable:   {total_used}")
    print("=================================\n")


if __name__ == "__main__":
    print(" CALCULADORA DE SUBNETTING Y VLSM\n")

    while True:
        print("1) Subnet Calculator")
        print("2) VLSM Planner")
        print("3) Salir")
        option = input("Selecciona opción: ")

        if option == "1":
            net = input("Ingresa red (ejemplo 192.168.1.0/24): ")
            subnet_info(net)

        elif option == "2":
            base = input("Red base (ejemplo 192.168.0.0/24): ")
            hosts = input("Ingresa hosts separados por coma (Ej: 100,50,10): ")
            host_list = [int(h.strip()) for h in hosts.split(",")]
            vlsm(base, host_list)

        elif option == "3":
            break

        else:
            print("Opción inválida\n")
