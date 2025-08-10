


import os

def process_file(input_file, output_file):
    """
    Reads from input_file, processes text (uppercase), and writes to output_file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
            print("\n--- Original Content ---")
            print(content)

       
        processed_content = content.upper()

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(processed_content)

        print(f"\n✅ Processed content written to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read/write this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def count_word_frequency(file_path):
    """
    Reads a text file and counts the frequency of each word (case-insensitive).
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        for char in "!@#$%^&*()_+-=,./<>?;:'\"[]{}|`~":
            text = text.replace(char, " ")

        words = text.lower().split()
        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        print("\n--- Word Frequency ---")
        for word, count in sorted(frequency.items()):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"❌ Unexpected error while counting words: {e}")


if __name__ == "__main__":
   
    input_filename = "input.txt"
    output_filename = "output.txt"

    
    if not os.path.exists(input_filename):
        with open(input_filename, 'w', encoding='utf-8') as f:
            f.write("Hello world! This is a sample file.\nThis file will be processed.")

    
    process_file(input_filename, output_filename)

    count_word_frequency(input_filename)
