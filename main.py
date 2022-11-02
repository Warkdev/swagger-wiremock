import json
import re
import random
import string

def get_random_int(min, max):
    return random.randint(min, max)


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


file_path = 'swagger-35.json'

with open(file=file_path, mode='rb') as stream:
    swagger_file = json.load(fp=stream)

base_path = swagger_file['basePath']
basic_auth = False
for sec_def in swagger_file['securityDefinitions']:
    if swagger_file['securityDefinitions'][sec_def]['type'] == 'basic':
        basic_auth = True

parameters = {}
assigned_params = {}

for path in swagger_file['paths']:
    top_level = path.split('/')[1]
    path_params = re.findall('{(.*?)}', path)
    param_def = swagger_file['paths'][path].get('parameters', [])
    for parameter in param_def:
        if '$ref' in parameter:
            p = parameter['$ref'].rsplit('/', 1)[1]
            if not p in parameters:
                parameters[swagger_file['parameters'][p]['name']] = swagger_file['parameters'][p]
        elif 'name' in parameter:
            if not parameter['name'] in parameters:
                parameters[parameter['name']] = parameter
    
    for path_param in path_params:
        if path_param in parameters:
            continue  # Skip already assigned parameters
        if 'default' in parameters[path_param]:
            assigned_params[path_param] = parameters[path_param]['default']
        elif parameters[path_param]['type'] == 'string':
            assigned_params[path_param] = get_random_string(parameters[path_param]['maxLength'])
        elif parameters[path_param]['type'] == 'integer':
            assigned_params[path_param] = get_random_int(parameters[path_param]['minimum'], parameters[path_param]['maximum'])
    for method in ['get', 'put', 'post', 'delete', 'options', 'head', 'patch']:
        if method in swagger_file['paths'][path]:
            if 'parameters' in swagger_file['paths'][path][method]:
                for parameter in swagger_file['paths'][path][method]['parameters']:
                    if '$ref' in parameter:
                        p = parameter['$ref'].rsplit('/', 1)[1]
                        if not p in parameters:
                            parameters[swagger_file['parameters'][p]['name']] = swagger_file['parameters'][p]
                            p_name = swagger_file['parameters'][p]['name']
                            if p_name in assigned_params:
                                continue
                            if 'default' in parameters[swagger_file['parameters'][p]['name']]:
                                assigned_params[p_name] = parameters[swagger_file['parameters'][p]['name']]['default']
                            elif parameters[swagger_file['parameters'][p]['name']]['type'] == 'string':
                                if 'enum' in parameters[p_name]:
                                    assigned_params[p_name] = random.choice(parameters[p_name]['enum'])
                                else:
                                    assigned_params[p_name] = get_random_string(parameters[p_name]['maxLength'])
                            elif parameters[swagger_file['parameters'][p]['name']]['type'] == 'integer':
                                assigned_params[p_name] = get_random_int(parameters[p_name]['minimum'], parameters[p_name]['maximum'])
                    elif 'name' in parameter:
                        if parameter['name'] == 'json':
                            print('Should generate some JSON body here')
                            continue
                        if not parameter['name'] in parameters:
                            parameters[parameter['name']] = parameter
                        if parameter['name'] in assigned_params:
                            continue
                        if 'default' in parameter:
                            assigned_params[parameter['name']] = parameter['default']
                        elif parameter['type'] == 'string':
                            if 'enum' in parameter:
                                assigned_params[parameter['name']] = random.choice(parameter['enum'])
                            elif 'maxLength' in parameter:
                                assigned_params[parameter['name']] = get_random_string(parameter['maxLength'])
                        elif parameter['type'] == 'integer':
                            assigned_params[parameter['name']] = get_random_int(parameter['minimum'], parameter['maximum'])


print(assigned_params)