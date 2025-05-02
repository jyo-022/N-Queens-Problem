def word_counter(filename):  
    try:
        with open(filename, 'r') as file:  
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"The file '{filename}' has {word_count} words.") 
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")  

if __name__ == "__main__":
    filename = input("Enter the filename to count words: ")  
    word_counter(filename)  