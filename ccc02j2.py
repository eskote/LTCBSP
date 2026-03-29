# ccc02j2

word = ''
substring = 'or'
while word != 'quit!':
    
    # Get input from the user
    word = str(input())
    if len(word) > 64:
        break

    # Extract substring and base string
    word_substr = word[-2:]
    word_str = word.replace(word[-2:], '')

    # Evaluate substring match
    if word == 'quit!':
        break
    if word_substr == substring and len(word) > 4 and word[-3] not in ['a','e','i','o','u']:
        print(
            word_str + 'our'
        )
    else:
        print(word)