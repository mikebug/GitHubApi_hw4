#Mike Buglione I plegde my honor that I have abided by the stevens honor system

import requests
import json


def get_github_info(input):
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

if __name__ == '__main__':
    input = input('GitHub username: ')
    print(get_github_info(input))
