def eight_bit(s: str) -> str:
    unbin = s.replace('0b', '')
    return '0' * (8-len(unbin)) + unbin

def network_mask(m: int) -> str:
    mask = []
    n = 1
    while n < 32:
        if n <= m:
            mask.append('1')
        else:
            mask.append('0')
        if n % 8 == 0:
            mask.append('.')
        n += 1
    return str(''.join(mask))

def ipcalc(net: str) -> str:
    netmask = net.split('/')
    network = netmask[0]
    mask = int(netmask[1])

    net_oct = network.split('.')
    net_oct_bin = [eight_bit(str(bin(int(n)))) for n in net_oct]
    return str('.'.join(net_oct_bin)+'/' + network_mask(mask))

if __name__ == '__main__':
    default = '192.168.0.1/24'
    network = input(f'Type network[{default}]: ')
    if not network:
        network = default
    print(ipcalc(net = network))

