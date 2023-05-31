def extract_key_value_pairs(file_path):
    key_value_pairs = {}
    current_group = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith('BEGIN_GROUP'):
                current_group = line.split('=')[1].strip()
                key_value_pairs[current_group] = {}
            elif line.startswith('END_GROUP'):
                current_group = None
            elif line != 'END;':
                if '=' in line:
                    key, value = line.split('=')
                    key = key.strip()
                    value = value.strip().strip(';').strip('"')
                    if current_group:
                        key_value_pairs[current_group][key] = value
                    else:
                        key_value_pairs[key] = value
                elif current_group:
                    if key_value_pairs[current_group].get(key):
                        key_value_pairs[current_group][key] += line
                    else:
                        key_value_pairs[current_group][key] = line

    return key_value_pairs


def list_all_key_value_pairs(key_value_pairs, indent=''):
    for key, value in key_value_pairs.items():
        if isinstance(value, dict):
            # print(f"{indent}{key}:")
            list_all_key_value_pairs(value, indent + '  ')
        elif isinstance(value, str):
            print(f"{indent}{key}: {value}")
        elif isinstance(value, list):
            if value:
                print(f"{indent}{key}:")
                for item in value:
                    print(f"{indent}  {item}")
            else:
                print(f"{indent}{key}: []")



# Usage example
file_path = './GF1B_PMS_E7.5_N35.8_20230315_L1A1228268087-MUX.rpb'
key_value_pairs = extract_key_value_pairs(file_path)
list_all_key_value_pairs(key_value_pairs)

a = key_value_pairs.items()

print(a)
