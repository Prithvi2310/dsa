def string_operation(word_list):
    new_list = []
    vowel_list = ['a','e','i','o','u']
    for word in word_list:
        new_word = word[1:]
        new_word += word[0]
        if word[0].lower() in vowel_list:
            new_word += "ay"
        else:
            new_word += "ed"
        new_list.append(new_word)
        
    return " ".join(new_list)
        

if __name__ == "__main__":
    word_list = [x for x in input("Enter text: ").split()]
    mystring = string_operation(word_list)
    print(mystring)