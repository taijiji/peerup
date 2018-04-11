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


def check_hostname(param):
    print('Check Hostname', end='')
    print(Fore.GREEN + 'OK')


def check_model(param):
    print('Check Model : ', end='')
    print(Fore.GREEN + 'OK')



def check_os_version(param):
    print('Check OS Version : ', end='')
    print(Fore.GREEN + 'OK')



def check_interface(param):
    print('Check Interface : ', end='')
    print(Fore.GREEN + 'OK')



def check_bgp_neighbor(param):
    print('Check BGP Neighbor : ', end='')
    print(Fore.GREEN + 'OK')



def check_bgp_route_received(param):
    print('Check BGP Roue Received : ', end='')
    print(Fore.GREEN + 'OK')



def check_bgp_route_advertised(param):
    print('Check BGP Roue Adcertised : ', end='')
    print(Fore.GREEN + 'OK')



def set_interface(param):
    print('Set Interface : ', end='')
    print(Fore.GREEN + 'OK')



def set_bgp_neighbor(param):
    print('Set BGP Neighbor : ', end='')
    print(Fore.GREEN + 'OK')



def set_bgp_route_received(param):
    print('Set BGP Route Recieved : ', end='')
    print(Fore.GREEN + 'OK')


def set_bgp_route_advertised(param):
    print('Set BGP Route Advertised : ', end='')
    print(Fore.GREEN + 'OK')



def exec_scenario(operation_list):
    for operation in operation_list:
        print(operation)


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
    '''
    driver = napalm.get_network_driver(param['hosts']['os'])
    device = driver(
                hostname=param['hosts']['mgmt_ipaddress'],
                username=param['username'],
                password=param['password'])
    device.open()
    '''
    print(Fore.GREEN + 'OK')


    print('===== Run Scenario =====')
    exec_scenario(param['scenario'])
