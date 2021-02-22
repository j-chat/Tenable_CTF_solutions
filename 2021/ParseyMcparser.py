'''
:param blob: blob of data to parse through (string)
:param group_name: A single Group name ("Green", "Red", or "Yellow",etc...)

:return: A list of all user names that are part of a given Group
'''
import re

def ParseNamesByGroup(blob, group_name):
    username_list = []
    brackets_list = re.findall('\[.*?\]',blob)
    for n in range(len(brackets_list)):
        if group_name in brackets_list[n]:
            split_by_comma = brackets_list[n].split(",")
            get_username = (split_by_comma[1].split(":")[1]).replace('"','')
            username_list.append(get_username)
    return username_list
   
data = raw_input()
group_name = data.split('|')[0]
blob = data.split('|')[1]
result_names_list = ParseNamesByGroup(blob, group_name)
print result_names_list
