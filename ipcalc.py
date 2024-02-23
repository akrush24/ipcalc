def eight_bit(s: str, pref = '') -> str:
    unbin = s.replace('0b', '')
    if pref == '0':
        return f'{unbin:0>8}'
    else:
        return f'{unbin:>8}'

def network_mask(m: int, bin = True) -> list:
    mask, maskstr = [], []
    n = 1
    while n < 32:
        if n <= m:
            mask.append('1')
        else:
            mask.append('0')
        if n % 8 == 0:
            maskstr.append(''.join(mask))
            mask = []
        n += 1
    maskstr.append(''.join(mask))
    # maskstr = str(''.join(mask)).split('.')
    return maskstr if bin else [ str(int(n, 2)) for n in maskstr ]

if __name__ == '__main__':
    default_netmask = '192.168.0.10/32'
    default_mask = '24'
    network = input(f'Type network [{default_netmask}]: ')
    if not network:
        network = default_netmask
    netmask = network.split('/')

    if len(netmask) == 1:
        mask = int(input(f'Enter the subnet mask [{default_mask}]: '))
    else:
        mask = int(netmask[1])
    network = netmask[0]

    net_oct = network.split('.')
    net_oct_bin = [eight_bit(str(bin(int(n))), '0') for n in net_oct]
    print(f'IP:   {str('.'.join(net_oct_bin))}')
    print(f'      {'.'.join([eight_bit(n) for n in network.split('.')])}')
    print(f'MAKS: {'.'.join([eight_bit(n, '0') for n in network_mask(mask, True)])}')
    print(f'      {'.'.join([eight_bit(n) for n in network_mask(mask, False)])}')
