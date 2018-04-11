import yaml
import napalm

# For Color Font
from colorama import init as colorama_init
from colorama import Fore

import sys
from pprint import pprint

# Init Color Font
colorama_init(autoreset=True)


def load_scenario_file(scenario_filename):
    with open(scenario_filename, 'r') as file:
        param_yaml = file.read()

    param = yaml.load(param_yaml)

    return param


def check_hostname(device, param):
    print('Check Hostname : ', end='')

    hostname_expected   = param['hostname']
    hostname_actual     = device.get_facts()['hostname']

    if hostname_actual == hostname_expected:
        print(Fore.GREEN + 'OK')
        print(Fore.GREEN + 'expected : ' +  hostname_expected)
        print(Fore.GREEN + 'actual   : ' +  hostname_actual)
    else:
        print(Fore.RED + 'NG')
        print(Fore.RED + 'expected : ' +  hostname_expected)
        print(Fore.RED + 'actual   : ' +  hostname_actual)


def check_model(device, param):
    print('Check Model : ', end='')

    model_expected   = param['model']
    model_actual     = device.get_facts()['model']

    if model_actual == model_expected:
        print(Fore.GREEN + 'OK')
        print(Fore.GREEN + 'expected : ' +  model_expected)
        print(Fore.GREEN + 'actual   : ' +  model_actual)
    else:
        print(Fore.RED + 'NG')
        print(Fore.RED + 'expected : ' +  model_expected)
        print(Fore.RED + 'actual   : ' +  model_actual)


def check_os_version(device, param):
    print('Check OS Version : ', end='')
    os_version_expected   = param['os_version']
    os_version_actual     = device.get_facts()['os_version']

    if os_version_actual == os_version_expected:
        print(Fore.GREEN + 'OK')
        print(Fore.GREEN + 'expected : ' +  os_version_expected)
        print(Fore.GREEN + 'actual   : ' +  os_version_actual)
    else:
        print(Fore.RED + 'NG')
        print(Fore.RED + 'expected : ' +  os_version_expected)
        print(Fore.RED + 'actual   : ' +  os_version_actual)


def check_interface(device, param):
    print('Check Interface : ', end='')

    if_status_expected = param['if_status']
    if_status_tmp = device.get_interfaces()[param['if_name']]['is_up']

    if if_status_tmp == True:
        if_status_actual   = 'up'
    elif if_status_tmp == False:
        if_status_actual   = 'down'
    
    if if_status_actual == if_status_expected:
        print(Fore.GREEN + 'OK')
        print(Fore.GREEN + 'expected : ' +  if_status_expected)
        print(Fore.GREEN + 'actual   : ' +  if_status_actual)
    else:
        print(Fore.RED + 'NG')
        print(Fore.RED + 'expected : ' +  if_status_expected)
        print(Fore.RED + 'actual   : ' +  if_status_actual)


def check_bgp_neighbor(device, param):
    print('Check BGP Neighbor : ', end='')
    neighbor_status_expected = param['neighbor_status']
    neighbor_status_tmp = device.get_bgp_neighbors()['global']['peers'][param['neighbor_addr']]['is_up']
    
    if neighbor_status_tmp == True:
        neighbor_status_actual   = 'up'
    elif neighbor_status_tmp == False:
        neighbor_status_actual   = 'down'
    
    if neighbor_status_actual == neighbor_status_expected:
        print(Fore.GREEN + 'OK')
        print(Fore.GREEN + 'expected : ' +  neighbor_status_expected)
        print(Fore.GREEN + 'actual   : ' +  neighbor_status_actual)
    else:
        print(Fore.RED + 'NG')
        print(Fore.RED + 'expected : ' +  neighbor_status_expected)
        print(Fore.RED + 'actual   : ' +  neighbor_status_actual)


def check_bgp_route_received(device, param):
    print('Check BGP Roue Received : ', end='')
    received_route_num_expected = param['received_route_num']
    received_route_num_actual =\
        device.get_bgp_neighbors()['global']['peers'][param['neighbor_addr']]['address_family']['ipv4']['received_prefixes']
    if received_route_num_actual == received_route_num_expected:
        print(Fore.GREEN + 'OK')
        print(Fore.GREEN + 'expected : ' + str(received_route_num_expected))
        print(Fore.GREEN + 'actual   : ' + str(received_route_num_actual))
    else:
        print(Fore.RED + 'NG')
        print(Fore.RED + 'expected : ' +  str(received_route_num_expected))
        print(Fore.RED + 'actual   : ' +  str(received_route_num_actual))
    
    '''
    if device.get_facts()['vendor'] == 'Juniper':
        commands_junos = 'show route receive-protocol bgp ' + param['neighbor_addr']
        cli_result = device.cli([commands_junos])
        print(Fore.YELLOW + 'Reulst: ' + commands_junos)
        print(Fore.YELLOW + str(cli_result[commands_junos]))
    else:
        pass
    '''


def check_bgp_route_advertised(device, param):
    print('Check BGP Roue Adcertised : ', end='')
    advertised_route_num_expected = param['advertised_route_num']
    advertised_route_num_actual =\
        device.get_bgp_neighbors()['global']['peers'][param['neighbor_addr']]['address_family']['ipv4']['sent_prefixes']
    if advertised_route_num_actual == advertised_route_num_expected:
        print(Fore.GREEN + 'OK')
        print(Fore.GREEN + 'expected : ' + str(advertised_route_num_expected))
        print(Fore.GREEN + 'actual   : ' + str(advertised_route_num_actual))
    else:
        print(Fore.RED + 'NG')
        print(Fore.RED + 'expected : ' +  str(advertised_route_num_expected))
        print(Fore.RED + 'actual   : ' +  str(advertised_route_num_actual))

    '''
    if device.get_facts()['vendor'] == 'Juniper':
        commands_junos = 'show route advertising-protocol bgp ' + param['neighbor_addr']
        cli_result = device.cli([commands_junos])
        print(Fore.YELLOW + 'Reulst: ' + commands_junos)
        print(Fore.YELLOW + str(cli_result[commands_junos]))
    else:
        pass
    '''



def set_interface(device, param):
    print('Set Interface : ', end='')
    print(Fore.GREEN + 'OK')



def set_bgp_neighbor(device, param):
    print('Set BGP Neighbor : ', end='')
    print(Fore.GREEN + 'OK')



def set_bgp_route_received(device, param):
    print('Set BGP Route Recieved : ', end='')
    print(Fore.GREEN + 'OK')


def set_bgp_route_advertised(device, param):
    print('Set BGP Route Advertised : ', end='')
    print(Fore.GREEN + 'OK')


def exec_scenario(device, operation_list):
    for operation in operation_list:
        opr_name  = list(operation.keys())[0]
        opr_param = operation[opr_name]

        if opr_name == 'check_hostname':
            check_hostname(device, opr_param)
        elif opr_name == 'check_model':
            check_model(device, opr_param)
        elif opr_name == 'check_os_version':
            check_os_version(device, opr_param)
        elif opr_name == 'check_interface':
            check_interface(device, opr_param)    
        elif opr_name == 'check_bgp_neighbor':
            check_bgp_neighbor(device, opr_param)
        elif opr_name == 'check_bgp_route_received':
            check_bgp_route_received(device, opr_param)
        elif opr_name == 'check_bgp_route_advertised':
            check_bgp_route_advertised(device, opr_param)
        elif opr_name == 'set_interface':
            set_interface(device, opr_param)
        '''
        elif opr_name == 'set_bgp_neighbor':
            set_bgp_neighbor(device, opr_param)
        elif opr_name == 'set_bgp_route_received':
            set_bgp_route_received(device, opr_param)
        elif opr_name == 'set_bgp_route_advertised':
            set_bgp_route_advertised(device, opr_param)
        '''
        


if __name__ == '__main__':

    scenario_filename = 'scenarios/scenario_demo_vsrx.yml'

    param = load_scenario_file(scenario_filename)
    #pprint(param)


    print('===== Operation Information =====')
    print('purpus:')
    print(param['purpus'])
    print('Operator        : ' + param['operator'])
    print('Operation Date  : ' + str(param['operation_date']))


    print('===== Host Information =====')
    print('Host Name        : ' + param['hosts']['hostname'])
    print('os               : ' + param['hosts']['os'])
    print('User Name        : ' + param['hosts']['username'])
    print('Password         : ' + param['hosts']['password'])
    print('mgmt_ipaddress   : ' + param['hosts']['mgmt_ipaddress'])


    print('===== Login Router =====')
    print("login router : ", end='')
    driver = napalm.get_network_driver(param['hosts']['os'])
    device = driver(
                hostname=param['hosts']['mgmt_ipaddress'],
                username=param['hosts']['username'],
                password=param['hosts']['password'])
    device.open()
    print(Fore.GREEN + 'OK')


    print('===== Run Scenario =====')
    exec_scenario(device, param['scenario'])
