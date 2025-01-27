def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_data = process_content(file_contents)
    char_data = get_chars_dict(file_contents)
    char_list = [{"char": char, "count": count} for char, count in char_data.items()]
    char_list.sort(key=lambda x: x["count"], reverse=True)


    print(f"Total number of words: {word_data['word_count']}")
    print("\nCharacter frequencies:")
    for char, count in sorted(char_data.items()):
        print(f"Character '{char}': {count} times")
    
def process_content(file_contents):
    words = file_contents.split()

    return {
        "word_count": len(words)
    }

def get_chars_dict(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

if __name__ == "__main__":
    main()