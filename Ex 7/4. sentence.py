import re

def sentence_grammar(sentence):
    # Define verbs
    verbs = ['cuts', 'sing', 'dance', 'fell', 'beat', 'drinks', 'ate']

    # Define subjects
    subjects = ['People', 'boys', 'girls', 'He', 'She', 'Ram', 'Kavin', 'Mohan', 'milk', 'child']

    # Define pronouns
    pronouns = ['I', 'You', 'He', 'She', 'It', 'We', 'They']

    # Define objects
    objects = ['tree', 'Lollypop', 'milk', 'cat']
    
    # Define articles
    articles = ['a', 'an', 'the']

    # Construct the regular expression pattern
    pattern = re.compile(fr"({'|'.join(map(re.escape, articles))})?.?({'|'.join(map(re.escape, subjects + pronouns))}).?({'|'.join(map(re.escape, verbs))}).?({'|'.join(map(re.escape, articles))})?.?({'|'.join(map(re.escape, objects))}).?$", re.IGNORECASE)

    # Check if at least one match is found in the sentence
    return bool(pattern.search(sentence))

if __name__ == '__main__':
    # Sample Test Cases
    print(sentence_grammar("Ram Cuts the tree."))  # Valid
    print(sentence_grammar("Mohan beat Kavin."))   # Invalid
    print(sentence_grammar("A child ate Lollypop."))  # Valid
    print(sentence_grammar("Drink milk cat."))   # Invalid
    print(sentence_grammar("Milk drinks cat."))  # Valid
