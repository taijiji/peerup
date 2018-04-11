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
    pprint(param)