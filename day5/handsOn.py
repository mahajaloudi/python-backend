def remove_duplicates(words: list) -> set:
  
    return set(word.lower() for word in words)


def count_word_frequency(words: list) -> dict:
   
    word_count = {}
    for word in words:
        word = word.lower() 
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


if __name__ == "__main__":
   
    text = "apple banana Apple orange banana apple grape"
    words_list = text.split()

    
    unique_words = remove_duplicates(words_list)
    print("Unique words:", unique_words)


    frequency = count_word_frequency(words_list)
    print("Word frequency:")
    for word, count in frequency.items():
        print(f"{word}: {count}")
