#We have the string like "AAA BBB CCC DDD EEE FFF GGG"
#The task is to split the string into words, to sort them in the reversed order an to translate into English
def revline(line):
    #line = "AAA BBB CCC DDD EEE FFF GGG"
    a = line.split(' ')
    a.sort(reverse = True)
    return a
print(revline("AAA BBB CCC DDD EEE FFF GGG"))

