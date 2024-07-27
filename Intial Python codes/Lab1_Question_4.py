import random
class TextGenerator:
    def __init__(self):
        self.prefix_dict={} # the prefix dictionary 
        
    def assimilateText(self,file_name):
        self.file_name=file_name
        my_file = open(self.file_name,"r+")
        content=my_file.read()  
        content_split = content.split() # split() is used to split the text into indivdual words

        # A dictionary is created with each two tuples as keys and the corresponding values 
        # are intialized as an empty list 
        self.prefix_dict={(content_split[i-1],content_split[i]):[] for i in range(1,len(content_split))}
        
        # The values are poulated in the dictionary according to the keys
        for i in range(1, len(content_split) - 1):
            self.prefix_dict[(content_split[i - 1], content_split[i])].append(content_split[i + 1])
        my_file.close()
        return self

    def generateText(self,no_of_words,word=None):
        self.no_of_words=no_of_words
        self.word= word # the optional argument for the method
        
        word_list=[] # The output text is stored in this list
        
        s=[] # A dummy list of two entries to act as key for the dictionary
        
        if isinstance(word,str)==False:
          word_list=list(random.choice(list(self.prefix_dict.keys())))
        
        # Raising exception if the word is not found in the text 
        elif self.word not in [key[0] for key in self.prefix_dict.keys()]:
                try:
                  raise Exception('Unable to produce text with specified stat word')
                except Exception as inst:
                     print(type(inst))
                     print(inst) 
                exit()
        # if the word is found randomly choosing a key which has the word
        else:
               for key in self.prefix_dict.keys():
                  if (key[0]==self.word):
                    s.append(key)
               word_list=list(random.choice(s))
        
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
t.assimilateText("/home/avijit/Desktop/sem_2/sherlock.txt")
t.generateText(100,"considerable")

