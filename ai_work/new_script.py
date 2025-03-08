```python
import csv
from collections import Counter

def read_text_file(file_name):
    """
    Read a text file and return the content as a string.
    
    Args:
    file_name (str): The name of the text file to read.
    
    Returns:
    str: The content of the text file.
    """
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def count_word_frequencies(text):
    """
    Count the frequencies of each word in a given text.
    
    Args:
    text (str): The text in which to count word frequencies.
    
    Returns:
    dict: A dictionary where keys are words and values are their frequencies.
    """
    words = text.split()
    word_freq = Counter(words)
    return word_freq

def output_to_csv(word_freq, output_file):
    """
    Output word frequencies to a CSV file.
    
    Args:
    word_freq (dict): A dictionary where keys are words and values are their frequencies.
    output_file (str): The name of the CSV file to output the results.
    """
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'Frequency'])
        for word, freq in word_freq.items():
            writer.writerow([word, freq])

def main(input_file, output_file):
    """
    Main function to automate the task of counting word frequencies in a text file and outputting the results to a CSV file.
    
    Args:
    input_file (str): The name of the input text file.
    output_file (str): The name of the output CSV file.
    """
    text = read_text_file(input_file)
    word_freq = count_word_frequencies(text)
    output_to_csv(word_freq, output_file)

if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = 'output.csv'
    main(input_file, output_file)
```