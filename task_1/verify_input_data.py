from pprint import pprint
import re

'''
This module contain two variants of possible solution depending on how to
understand the task itself.
'''

test_text = '''{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''
list_keys = [
    'name',
    'day_month',
    'day_of_week',
    'start_time',
    'end_time',
    'master',
    'services',
]


# 1. Simplest case when we check if the keys from list_keys are present
# and they have opening and closing braces
def verify_data(test_text: str, list_keys: list[str]) -> str:
    result = []
    for k in list_keys:
        if '{' + k + '}' in test_text:
            result.append((k, 'Correct! The key is verified'))
        else:
            result.append((k, 'Wrong! The key is not verified'))
    return result


result = verify_data(test_text, list_keys)
pprint(result)


# 2. The case when we go deeper and make fuller verification
def verify_data(test_text, list_keys):
    # Check the presence of all keys from list_keys in the text
    for key in list_keys:
        if f'{{{key}}}' not in test_text:
            return f'Error: <{key}> is not present'

    # Check the correct format of the keys
    pattern = re.compile(r'{([a-z_]+)}', re.IGNORECASE)
    matches = pattern.findall(test_text)
    for match in matches:
        if match not in list_keys:
            return f'Error: incorrect key <{match}>'

    # Check the balance of opening and closing braces
    if (
        test_text.count('{') != test_text.count('}')
        or '{' in test_text
        and '}' not in test_text
    ):
        return 'Error: incorrect number of braces'

    return test_text  # Return the text if all checks pass


result = verify_data(test_text, list_keys)
print(result)
