#Mike Buglione I plegde my honor that I have abided by the stevens honor system

import requests
import json

input = u = input('GitHub username: ')
#input = mikebug

def main(input):
    if (input == "") or (not isinstance(input,str)):
        return "Invalid Inputs"
    else:
        repo = requests.get('https://api.github.com/users/' + input + '/repos')
        list = json.loads(repo.text)
    try:
        for i in list:
            name = i['name']
            c = requests.get('https://api.github.com/repos/' + input + '/' + name + '/commits')
            commits_data = len(c.json())
            print('Repository Name:' + name + ' Number of commits: ' + str(commits_data))
    except:
        pass
    return "End"


print(main(input))
