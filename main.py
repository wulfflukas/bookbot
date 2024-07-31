def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    count = word_count(text)
    char = char_count(text)
    sorted_list = sort_key(char)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in document")
    print()
    for i in sorted_list:
        print(f"The {i['char']}' character was found {i['num']} times")
    print("--- End report ---")
    
    
    
def get_text(path):
    with open(path) as f:
        return f.read()
def word_count(text):
    return len(text.split())

def char_count(text):
    count = {}
    text = text.lower()
    for letter in text: 
        if letter.isalpha():
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
    return count
def sort_value(count):
    return count["num"]
def sort_key(count):
    sorted_list = []
    for dik in count: 
        sorted_list.append({"char": dik, "num": count[dik]})
    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list
        
        

    
                

        
        
if __name__ == "__main__": 
    main()