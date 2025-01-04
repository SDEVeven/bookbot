def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() #string
    #print (type(file_contents))
    #print (f"Total Words: {Words(file_contents)}")
    #print (f"Total Characters: {Characters(file_contents)}")
    #print (f"Individual Characters: {count_Characters(file_contents)}")
    #book_report(Words(file_contents), count_Characters(file_contents))
    #print (f"Dichtonarry {count_Characters(file_contents)}")
    #print (f"List of Dichtonarry {to_ListDic(count_Characters(file_contents))}")
    book_report(Words(file_contents), sort_Individual_Characters(count_Characters(file_contents)))

def Words(string):
    return len(string.split())

def Characters(string):
    counter = 0 
    for i in string:
        counter +=1
    return counter

def count_Characters(book_string):
    lowercase = book_string.lower()
    character = {}
    for i in range (0, len(lowercase)):
        if lowercase[i] not in character and lowercase[i].isalpha() :  character[lowercase[i]] = 1
        elif lowercase[i].isalpha(): character[lowercase[i]] += 1
    return character

def sort_on(dict): #takes dictonarry and return "Amount" key value
    return dict["Amount"]

def to_ListDic(dict):
    a = []
    for i in dict:
        b={}
        b["Character"]=i
        b["Amount"]=dict[i]
        a.append(b)
    return a
def sort_Individual_Characters(individual_characters): #takes a dictonarry of the amound of the individual characters and returns it sorted
    list_dictonnary_individual_characters= to_ListDic(individual_characters)
    list_dictonnary_individual_characters.sort(reverse=True, key=sort_on)
    return list_dictonnary_individual_characters

def book_report(total_words, sorted_individual_characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print (f"{total_words} Words found in the document")
    print()
    for i in range(0,len(sorted_individual_characters)):
        print (f"the '{sorted_individual_characters[i]["Character"]}' character was found {sorted_individual_characters[i]["Amount"]} times")
    print("--- End report ---")
main()
