import json
from difflib import get_close_matches
data =json.load(open("data.json"));
while(1):
    def translate(w):
        if w in data:
            return data[w]
        elif len(get_close_matches(w,data.keys(), cutoff=0.8))>0:
            con=input("Did you mean %s instead:enter Y if yes or N if no " % get_close_matches(w,data.keys())[0] )
            if con=='Y':
                return data[get_close_matches(w,data.keys())[0]]
            elif con =='N':
                return "The word doesn't exist in our librery"
            else:
                print("Enter a valid choise")
                answer=translate(word.lower());
            
        else:
            return "The word doesn't exist in our librery"
    word=input("Enter the word: ");
    answer=translate(word.lower());
    if type(answer)==list:
        for i in answer:
            print(i+'\n')
    else:
        print(answer)
