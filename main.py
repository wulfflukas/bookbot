def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    count = word_count(text)
    char = char_count(text)
    print(text)
    print(count)
    print(char)
    
    
    
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
    
                

        
        
if __name__ == "__main__": 
    main()