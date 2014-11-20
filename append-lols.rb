#Retrieve your most recent git commit hash and message.
#Anything inside backticks will execute as a command in your shell
#The backtick is located above the tab key on your keyboard
commit = `git log -1 --oneline`

#Isolate the hash and the message.
hash = commit.to_s.split(" ").first
message = commit.sub("#{hash} ", "")

#Unless the commit message already has a link to a gif...
unless(message.gsub("\n","").end_with?(".gif"))

  #Create a gif with lolcommits!
  `lolcommits --capture --animate=3`

  #Find the path to your present working directory, the location
  #of your repo on GitHub, your present working directory name
  #and the path to which Lolcommits saves your gifs.
  repopath = `git rev-parse --show-toplevel`.gsub("\n", "")
  repourl = `git config --get remote.origin.url`.gsub("\n", "")
  reponame = "#{`basename #{repopath}`.to_s}".gsub("\n", "")
  path = "#{File.expand_path('~')}/.lolcommits/#{reponame}/"

  #Find the gif with a filename that begins with your latest
  #commit hash and create a directory in your repo for storing
  #lols and copy in the gif
  @filename = nil
  Dir.open(path).each do |filename|
    if filename.start_with?(hash)
      image = path + filename
      system("mkdir #{repopath}/lolcommits")
      `cp #{image} #{repopath}/lolcommits/#{filename}`
      @filename = filename
    end
  end

  #Grab your username and repo name, assemble the url GitHub
  #will save the gif to git add the gif and git commit with
  #an amended message
  unless @filename == nil
    githubstuff = repourl.gsub("git@github.com:","").gsub(".git","").gsub("https://github.com/","")
    github_image_url = "https://github.com/#{githubstuff}/blob/master/lolcommits/#{@filename}"
    `git add #{repopath}/lolcommits/#{@filename}`
    `git commit --amend --no-verify -m "#{message} #{github_image_url}"`
  end

end