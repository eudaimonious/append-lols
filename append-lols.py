#Retrieve your most recent git commit hash and message.
#Anything inside backticks will execute as a command in your shell
#The backtick is located above the tab key on your keyboard
import subprocess
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
  reponame = subprocess.check_output("basename {}".format(repopath).replace("\n", "")
  path = "#{File.expand_path('~')}/.lolcommits/#{reponame}/" # this line is still ruby ;-)
