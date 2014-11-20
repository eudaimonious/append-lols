import subprocess
import os
import shutil

from os import listdir
from os.path import expanduser
from time import sleep


#Retrieve your most recent git commit hash and message.
#Anything inside backticks will execute as a command in your shell
#The backtick is located above the tab key on your keyboard

commit = subprocess.check_output("git log -1 --oneline", shell=True)
print "commit: {}".format(commit)
#Isolate the hash and the message.
hash = str(commit).split(" ")[0]
print "hash: {}".format(hash)
message = commit.replace("{} ".format(hash), "")
print "message: {}".format(message)
#Unless the commit message already has a link to a gif...
if not message.replace("\n","").endswith(".gif"):

    #Create a gif with lolcommits!
    subprocess.call("lolcommits --capture --animate=3 --delay=3 --fork", shell=True)

    #Find the path to your present working directory, the location
    #of your repo on GitHub, your present working directory name
    #and the path to which Lolcommits saves your gifs.
    repopath = subprocess.check_output("git rev-parse --show-toplevel", shell=True).replace("\n", "")
    print "repopath: {}".format(repopath)
    repourl = subprocess.check_output("git config --get remote.origin.url", shell=True).replace("\n", "")
    print "repourl: {}".format(repourl)
    reponame = subprocess.check_output("basename {}".format(repopath), shell=True).replace("\n", "")
    print "reponame: {}".format(reponame)
    path = "{}/.lolcommits/{}/".format(expanduser("~"), reponame)
    print "path: {}".format(path)

    #Find the gif with a filename that begins with your latest
    #commit hash and create a directory in your repo for storing
    #lols and copy in the gif
    sleep()
    filename = None
    print "filename: {}".format(filename)
    for f in listdir(path):
        print "all files: {}".format(f)
        if f.startswith(hash):
            print "the chosen file: {}".format(f)
            image = path + f
            print "image: {}".format(image)
            dst =  "{}/lolcommits/{}".format(repopath, filename)
            print "dst: {}"
            shutil.copyfile(image, dst)
            filename = f
            print "filename: {}".format(filename)

    #Grab your username and repo name, assemble the url GitHub
    #will save the gif to git add the gif and git commit with
    #an amended message
    if filename:
        print "filename: {}".format(filename)
        githubstuff = repourl.replace("git@github.com:","").replace(".git","").replace("https://github.com/","")
        print "githubstuff: {}".format(githubstuff)
        github_image_url = "https://github.com/{}/blob/master/lolcommits/{}".format(githubstuff, filename)
        print "github_image_url: {}".format(github_image_url)
        subprocess.call("git add {}/lolcommits/{}".format(repopath, filename), shell=True)
        subprocess.call("git commit --amend --no-verify -m '{} #{}'".format(message, github_image_url), shell=True)
