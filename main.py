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
    
    pre = []
    for letter in text.lower():
        if letter.isalpha() and letter not in pre:
            pre.append(letter)
    pre = sorted(pre)
    count = {letter: 0 for letter in pre}
    for letter in text.lower():
        if letter.isalpha():
            count[letter] += 1
    return count
                

        
        
if __name__ == "__main__": 
    main()