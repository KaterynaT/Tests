#We have the string like "AAA BBB CCC DDD EEE FFF GGG"
#The task is to split the string into words, to sort them in the reversed order an to translate into English
def revline(line):
    #line = "AAA BBB CCC DDD EEE FFF GGG"
    a = line.split(' ')
    a.sort(reverse=True)
    return a

if __name__ == "__main__":
	print(revline("AAA BBB CCC DDD EEE FFF GGG"))
else:
    print('I am running as an imported module with name = %s' % __name__)
