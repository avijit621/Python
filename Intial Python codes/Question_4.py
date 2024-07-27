import random
class TextGenerator:
    def __init__(self):
        self.prefix_dict={}

    def assimilateText(self,file_name):
        self.file_name=file_name
        my_file = open(self.file_name, encoding="utf8")
        content=my_file.read()
        content_split = content.split()
        self.prefix_dict={(content_split[i-1],content_split[i]):[] for i in range(1,len(content_split))}
        for i in range(1, len(content_split) - 1):
            self.prefix_dict[(content_split[i - 1], content_split[i])].append(content_split[i + 1])
        my_file.close()
        #print(self.prefix_dict[("To","Sherlock")])
        return self
    def generateText(self,no_of_words,word=None):
        self.no_of_words=no_of_words
        self.word= word
        if word==None:
          word_list = list(random.choice(list(self.prefix_dict.keys())))
        else:
            for key in self.prefix_dict.keys():
                if (key[0]==self.word):
                   self.word_list.append(key)
        #print(word_list)
        if len(self.prefix_dict[tuple(word_list)]) >0:
            s=word_list
        while len(word_list) <=self.no_of_words:
            s=[word_list[len(word_list)-2],word_list[len(word_list)-1]]
            if (len(self.prefix_dict[tuple(s)]))==0:
                break
            word_list.append(random.choice(self.prefix_dict[tuple(s)]))
            s.clear()
        print(" ".join(word_list))


t=TextGenerator()
t.assimilateText("sherlock.txt")
t.generateText(100,'London')