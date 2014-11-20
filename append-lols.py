import subprocess
from os import listdir
from os.path import expanduser


#Retrieve your most recent git commit hash and message.
#Anything inside backticks will execute as a command in your shell
#The backtick is located above the tab key on your keyboard

commit = subprocess.check_output("git log -1 --oneline")

#Isolate the hash and the message.
hash = str(commit).split(" ")[0]
message = commit.replace("{} ".format(hash), "")

#Unless the commit message already has a link to a gif...
if not message.replace("\n","").endswith(".gif"):

    #Create a gif with lolcommits!
    subprocess.call("lolcommits --capture --animate=3 --delay=3 --fork")

    #Find the path to your present working directory, the location
    #of your repo on GitHub, your present working directory name
    #and the path to which Lolcommits saves your gifs.
    repopath = subprocess.check_output("git rev-parse --show-toplevel").replace("\n", "")
    repourl = subprocess.check_output("git config --get remote.origin.url").replace("\n", "")
    reponame = subprocess.check_output("basename {}".format(repopath)).replace("\n", "")
    path = "{}/.lolcommits/{}/".format(expanduser("~"), reponame)

    #Find the gif with a filename that begins with your latest
    #commit hash and create a directory in your repo for storing
    #lols and copy in the gif
    filename = None
    for f in listdir(path):
        if f.startwith(hash):
          image = path + f
          system("mkdir #{repopath}/lolcommits")
          subprocess.call("cp {} {}/lolcommits/{}".format(image, repopath, filename))
          filename = f

    #Grab your username and repo name, assemble the url GitHub
    #will save the gif to git add the gif and git commit with
    #an amended message
    if filename:
        githubstuff = repourl.replace("git@github.com:","").replace(".git","").replace("https://github.com/","")
        github_image_url = "https://github.com/{}/blob/master/lolcommits/{}".format(githubstuff, filename)
        subprocess.call("git add {}/lolcommits/{}".format(repopath, filename))
        subprocess.call("git commit --amend --no-verify -m '{} #{}'".format(message, github_image_url))
