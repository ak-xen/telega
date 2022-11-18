async def output_config(conf_dict):
    sample_config = {
        'Fiberhome S48020-10T-GF': f'''admin\n12345\nconfig\nusername admin password 100pass\nsnmp location {conf_dict['addr_station']}\nvlan {conf_dict['vlan']}\nalias management\nexit\ninterface vlan {conf_dict['vlan']}\nip addres {conf_dict['ip']}/{conf_dict['netmask']}\nexit\nip route-static 0.0.0.0 0.0.0.0 {conf_dict['gateway']}\ninterface gigaethernet 1/0/8 to  gigaethernet 1/0/10\nport hybrid vlan 1-4094 tag\nlldp admin-status rx-tx\nexit\nsnmp view all 1 included\nsnmp community orange rw view all\ninterface gigaethernet 1/0/1 to gigaethernet 1/0/7\nloop-check enable\nloop-check action shutdown\nloop-check shutdown recover-time 100\nstorm-suppression action error-down\nstorm-suppression multicast 64kbps 40\nstorm-suppression broadcast 64kbps 40\nexit\nstorm-suppression mode default\nstorm-suppression log enable\nstorm-suppression trap enable\nerror-down auto-recovery cause storm-suppression interval 30\nvlan-trunk enable\nend\nwrite file\ny'''
        , 'Fiberhome S48020-28T-GF': f'''admin
12345
config
username admin password 100pass
snmp location {conf_dict['addr_station']}
vlan {conf_dict['vlan']}
alias management
exit
interface vlan {conf_dict['vlan']}
ip addres {conf_dict['ip']}/{conf_dict['netmask']}
exit
ip route-static 0.0.0.0 0.0.0.0 {conf_dict['gateway']}
interface gigaethernet 1/0/25 to  gigaethernet 1/0/28
port hybrid vlan 1-4094 tag
lldp admin-status rx-tx
exit
snmp view all 1 included
snmp community orange rw view all
interface gigaethernet 1/0/1 to gigaethernet 1/0/24
loop-check enable
 loop-check action shutdown
 loop-check shutdown recover-time 100
 storm-suppression action error-down
 storm-suppression multicast 64kbps 40
 storm-suppression broadcast 64kbps 40
exit
storm-suppression mode default
 storm-suppression log enable
 storm-suppression trap enable
 error-down auto-recovery cause storm-suppression interval 30
vlan-trunk enable
end
write file
y'''
        , 'Fiberhome S48020-52T-GF': f'''admin
12345
config
username admin password 100pass
snmp location {conf_dict['addr_station']}
vlan {conf_dict['vlan']}
alias management
exit
interface vlan {conf_dict['vlan']}
ip addres {conf_dict['ip']}/{conf_dict['netmask']}
exit
ip route-static 0.0.0.0 0.0.0.0 {conf_dict['gateway']}
interface gigaethernet 1/0/49 to  gigaethernet 1/0/52
port hybrid vlan 1-4094 tag
lldp admin-status rx-tx
exit
snmp view all 1 included
snmp community orange rw view all
interface gigaethernet 1/0/1 to gigaethernet 1/0/48
loop-check enable
 loop-check action shutdown
 loop-check shutdown recover-time 100
 storm-suppression action error-down
 storm-suppression multicast 64kbps 40
 storm-suppression broadcast 64kbps 40
exit
storm-suppression mode default
 storm-suppression log enable
 storm-suppression trap enable
 error-down auto-recovery cause storm-suppression interval 30
vlan-trunk enable
end
write file
y'''
        , 'D-link DES-3200-26': f'''create account admin admin
100pass
100pass
create vlan management-{conf_dict['vlan']} tag {conf_dict['vlan']}
config ipif System ipaddress {conf_dict['ip']}/{conf_dict['netmask']} vlan management-{conf_dict['vlan']} state enable
create iproute default {conf_dict['gateway']}
config vlan management-2434 add tagged 25-26
config snmp system_location {conf_dict['addr_station']}
config traffic control 1-24 broadcast enable multicast enable unicast disable action drop threshold 128 countdown 5 time_interval 15
config traffic control 25-26 broadcast disable multicast disable unicast disable
enable loopdetect
config loopdetect ports 1-24 state enabled
config loopdetect ports 25-26 state disabled
disable stp
delete snmp community public
delete snmp community private
create snmp community orange view CommunityView read_write
enable snmp traps
enable snmp
enable lldp
config lldp ports 25-26 admin_status tx_and_rx
config lldp ports 25-26 basic_tlvs all enable
config lldp ports 25-26 mgt_addr ipv4 {conf_dict['ip']} enable
config ports 1-24 state disable
config snmp system_contact PORTS_DOWN
save'''
        , 'D-link DES-3200-26/C1': f'''create account admin admin
100pass
100pass
create vlan management-{conf_dict['vlan']} tag {conf_dict['vlan']}
config ipif System ipaddress {conf_dict['ip']}/{conf_dict['netmask']} vlan management-{conf_dict['vlan']} state enable
create iproute default {conf_dict['gateway']}
config vlan management-{conf_dict['vlan']} add tagged 25-26
config snmp system_location {conf_dict['addr_station']}
config traffic control 1-24 broadcast enable multicast enable unicast disable action drop threshold 128 countdown 5 time_interval 15
config traffic control 25-26 broadcast disable multicast disable unicast disable action drop threshold 64 countdown 0 time_interval 5
enable loopdetect
config loopdetect ports 1-24 state enabled
config loopdetect ports 25-26 state disabled
disable stp
delete snmp community public
delete snmp community private
create snmp community orange view CommunityView read_write
enable snmp traps
enable snmp
enable lldp
config lldp ports 25-26 admin_status tx_and_rx
config lldp ports 25-26 basic_tlvs all enable
config lldp ports 25-26 mgt_addr ipv4 {conf_dict['ip']} enable
config ports 1-24 state disable
config snmp system_contact PORTS_DOWN
save'''
        , 'D-link DES-3200-28/C1A': f'''create account admin admin
100pass
100pass
create vlan management-{conf_dict['vlan']} tag {conf_dict['vlan']}
config ipif System ipaddress {conf_dict['ip']}/{conf_dict['netmask']} vlan management-{conf_dict['vlan']} state enable
create iproute default {conf_dict['gateway']}
config vlan management-{conf_dict['vlan']} add tagged 25-28
config snmp system_location {conf_dict['addr_station']}
config traffic control 1-24 broadcast enable multicast enable unicast disable action drop threshold 128 countdown 5 time_interval 15
config traffic control 25-28 broadcast disable multicast disable unicast disable action drop threshold 64 countdown 0 time_interval 5
enable loopdetect
config loopdetect ports 1-24 state enabled
config loopdetect ports 25-28 state disabled
disable stp
delete snmp community public
delete snmp community private
create snmp community orange view CommunityView read_write
enable snmp traps
enable snmp
enable lldp
config lldp ports 25-28 admin_status tx_and_rx
config lldp ports 25-28 basic_tlvs all enable
config lldp ports 25-28 mgt_addr ipv4 {conf_dict['ip']} enable
config ports 1-24 state disable
config snmp system_contact PORTS_DOWN
save'''
        , 'D-link DES-3200-52/C1': f'''create account admin admin
100pass
100pass
create vlan management-{conf_dict['vlan']} tag {conf_dict['vlan']}
config ipif System ipaddress {conf_dict['ip']}/{conf_dict['netmask']} vlan management-{conf_dict['vlan']} state enable
create iproute default {conf_dict['gateway']}
config vlan management-{conf_dict['vlan']} add tagged 49-52
config snmp system_location {conf_dict['addr_station']}
config traffic control 1-48 broadcast enable multicast enable unicast disable action drop threshold 128 countdown 5 time_interval 15
config traffic control 49-52 broadcast disable multicast disable unicast disable action drop threshold 64 countdown 0 time_interval 5
enable loopdetect
config loopdetect ports 1-48 state enabled
config loopdetect ports 49-52 state disabled
disable stp
delete snmp community public
delete snmp community private
create snmp community orange view CommunityView read_write
enable snmp traps
enable snmp
enable lldp
config lldp ports 49-52 admin_status tx_and_rx
config lldp ports 49-52 basic_tlvs all enable
config lldp ports 49-52 mgt_addr ipv4 {conf_dict['ip']} enable
config ports 1-48 state disable
config snmp system_contact PORTS_DOWN
save'''
    }
    return sample_config[list(conf_dict.values())[0]]


async def config_file(addr, com, ip, text):
    addr = await transliteration(addr)
    com = '_'.join(com.split())
    com = com.replace('/', ':')
    name_file = f'{addr}_{com}_{ip}'
    path = fr'data/config_data/temp/{name_file}.cfg'
    await make_file(path, text)
    return path


async def make_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)
        file.close()


async def transliteration(addr):
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'cz', 'ш': 'sh', 'щ': 'scz', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'u', 'я': 'ja', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
              'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'C', 'Ч': 'CZ', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'U', 'Я': 'YA'}
    for key in slovar:
        addr = addr.replace(key, slovar[key])
    addr = '_'.join(addr.split())
    return addr
