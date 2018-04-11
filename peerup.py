import yaml
import napalm
from jinja2 import Template, Environment

# For Color Font
from colorama import init as colorama_init
from colorama import Fore

import sys
import time
from pprint import pprint

# Init Color Font
colorama_init(autoreset=True)


def load_scenario_file(scenario_filename):
    with open(scenario_filename, 'r') as file:
        param_yaml = file.read()

    param = yaml.load(param_yaml)

    return param


def generate_from_jinja2(template_filename, template_param):
        # read template file (jinja2 format)
        with open(template_filename, 'r') as f:
            template_jinja2 = f.read()

        # generate nwtest file from template file
        return Environment().from_string(template_jinja2).render(template_param)
        


def check_hostname(device, param):
    print('-'*30)
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
    print('-'*30)
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
    print('-'*30)
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
    print('-'*30)
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
    print('-'*30)
    print('Check BGP Neighbor : ', end='')

    neighbor_status_expected = param['neighbor_status']

    if device.get_bgp_neighbors() == {}:
        neighbor_status_tmp = False
    else:
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
    print('-'*30)
    print('Check BGP Roue Received : ', end='')
    
    received_route_num_expected = param['received_route_num']
    
    if device.get_bgp_neighbors() == {}:
        received_route_num_actual = 0
    else:        
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
    print('-'*30)
    print('Check BGP Roue Adcertised : ', end='')

    advertised_route_num_expected = param['advertised_route_num']
    
    if device.get_bgp_neighbors() == {}:
        advertised_route_num_actual = 0
    else:        
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
    print('-'*30)
    print('Set Interface : ')

    print('--- Generate Config ---')
    template_filename = 'config_templates/junos/interface_add.jinja2'
    config_txt = generate_from_jinja2(template_filename, param)
    print(Fore.YELLOW + config_txt)

    print('--- Load Config ---')
    device.load_merge_candidate(config=config_txt)
    print('Load: ', end='')
    print(Fore.GREEN + 'OK')

    print('--- Compare Diff ---', end='')
    print(Fore.YELLOW + device.compare_config())

    print('--- Commit ---')
    print(Fore.YELLOW + "Do you commit? y/n")
    choice = input()
    if choice == "y":
        print("Commit config: ", end="")
        device.commit_config()
        print(Fore.GREEN + "OK")
    else:
        print("Discard config: ", end="")
        device.discard_config()
        print(Fore.GREEN + "OK")

    time.sleep(3) #実行完了を待つ処理。


def set_bgp_neighbor(device, param):
    print('-'*30)
    print('Set BGP Neighbor : ')

    print('--- Generate Config ---')
    template_filename = 'config_templates/junos/bgp_neighbor_add.jinja2'
    config_txt = generate_from_jinja2(template_filename, param)
    print(Fore.YELLOW + config_txt)

    print('--- Load Config ---')
    device.load_merge_candidate(config=config_txt)
    print('Load: ', end='')
    print(Fore.GREEN + 'OK')

    print('--- Compare Diff ---')
    print(Fore.YELLOW + device.compare_config())

    print('--- Commit ---')
    print(Fore.YELLOW + "Do you commit? y/n")
    choice = input()
    if choice == "y":
        print("--- Commit config ---")
        device.commit_config()
        print(Fore.GREEN + "OK")
    else:
        print("--- Discard config ---")
        device.discard_config()
        print(Fore.GREEN + "OK")

    time.sleep(3) #実行完了を待つ処理。


def set_bgp_route_advertised(device, param):
    print('-'*30)
    print('Set BGP Route Advertised : ', end='')
    
    print('--- Generate Config ---')
    template_filename = 'config_templates/junos/routepolicy_out_change.jinja2'
    config_txt = generate_from_jinja2(template_filename, param)
    print(Fore.YELLOW + config_txt)

    print('--- Load Config ---')
    device.load_merge_candidate(config=config_txt)
    print('Load: ', end='')
    print(Fore.GREEN + 'OK')

    print('--- Compare Diff ---')
    print(Fore.YELLOW + device.compare_config())

    print('--- Commit ---')
    print(Fore.YELLOW + "Do you commit? y/n")
    choice = input()
    if choice == "y":
        print("--- Commit config ---")
        device.commit_config()
        print(Fore.GREEN + "OK")
    else:
        print("--- Discard config ---")
        device.discard_config()
        print(Fore.GREEN + "OK")

    time.sleep(3) #実行完了を待つ処理。


def set_bgp_route_received(device, param):
    print('-'*30)
    print('Set BGP Route Recieved : ', end='')
    
    print('--- Generate Config ---')
    template_filename = 'config_templates/junos/routepolicy_in_change.jinja2'
    config_txt = generate_from_jinja2(template_filename, param)
    print(Fore.YELLOW + config_txt)

    print('--- Load Config ---')
    device.load_merge_candidate(config=config_txt)
    print('Load: ', end='')
    print(Fore.GREEN + 'OK')

    print('--- Compare Diff ---')
    print(Fore.YELLOW + device.compare_config())

    print('--- Commit ---')
    print(Fore.YELLOW + "Do you commit? y/n")
    choice = input()
    if choice == "y":
        print("--- Commit config ---")
        device.commit_config()
        print(Fore.GREEN + "OK")
    else:
        print("--- Discard config ---")
        device.discard_config()
        print(Fore.GREEN + "OK")

    time.sleep(3) #実行完了を待つ処理。


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
        elif opr_name == 'set_bgp_neighbor':
            set_bgp_neighbor(device, opr_param)
        elif opr_name == 'set_bgp_route_received':
            set_bgp_route_received(device, opr_param)
        elif opr_name == 'set_bgp_route_advertised':
            set_bgp_route_advertised(device, opr_param)


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

    print('===== All Processes Completed!! =====')
