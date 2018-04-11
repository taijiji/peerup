import yaml
import napalm

# For Color Font
from colorama import init as colorama_init
from colorama import Fore

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
    print(Fore.GREEN + 'OK')



def check_os_version(device, param):
    print('Check OS Version : ', end='')
    print(Fore.GREEN + 'OK')



def check_interface(device, param):
    print('Check Interface : ', end='')
    print(Fore.GREEN + 'OK')



def check_bgp_neighbor(device, param):
    print('Check BGP Neighbor : ', end='')
    print(Fore.GREEN + 'OK')



def check_bgp_route_received(device, param):
    print('Check BGP Roue Received : ', end='')
    print(Fore.GREEN + 'OK')



def check_bgp_route_advertised(device, param):
    print('Check BGP Roue Adcertised : ', end='')
    print(Fore.GREEN + 'OK')



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
        opr_name  = next(iter(operation))
        opr_param = operation[opr_name]
        #print(opr_name)

        if opr_name == 'check_hostname':
            check_hostname(device, opr_param)
        elif opr_name == 'check_model':
            check_model(device, opr_param)


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
