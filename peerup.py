import yaml
from pprint import pprint

def load_scenario_file(scenario_filename):
    with open(scenario_filename, 'r') as file:
        param_yaml = file.read()

    param = yaml.load(param_yaml)

    return param


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


