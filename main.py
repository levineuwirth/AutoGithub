import os
import datetime
import git

def main():
    repo_file = open('repos.txt', 'r')
    config_file = open('config.txt', 'r')
    repo_list = repo_file.readlines()

    ### Remove the comments 
    for line in repo_list:
        if(line[0] == '#'):
            repo_list.remove(line)

    config_lines = config_file.readlines()
    threshold = int(config_lines[1])
    time = int(config_lines[2])

    logs = open('logs.txt', 'a')
    logs.write("Program Started at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

    
    print("Program is Active")

    while True:
        time.sleep(threshold)
        for line in repo_list:
            repo = git.Repo(line)
            if repo.is_dirty:
                repo.git.add(update=True)
                repo.index.commit("Auto Commit: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                origin = repo.remote(name='origin')
                origin.push()
                print("Changes pushed for " + repo.working_dir)
                logs.write("Changes pushed for " + repo.working_dir + " at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                
