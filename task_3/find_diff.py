from json_new import json_new
from json_old import json_old
from diff_list import diff_list


# Unfortunately, I didn't solve this task properly. This solution is suitable
# only for special case when incoming data (json_old and json_new) has 'data'
# keys in them
result = {}
for key in diff_list:
    if (
        key in json_old['data']
        and key in json_new['data']
        and json_old['data'][key] != json_new['data'][key]
    ):
        result[key] = json_new['data'][key]

print(f'Result: {result}')
