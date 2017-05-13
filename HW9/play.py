with open("small_wordlist.txt","r") as f:
    a = f.readlines()
    for i in a:
        w = open("play.txt","w")
        w.write(i)
        w.close()
