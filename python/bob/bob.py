"""
Bob is a lackadaisical teenager. In conversation, his responses are very limited
"""
def response(hey_bob):
    """
    Bob's responses to different inputs
    :param hey_bob: input string
    :return: Bob's response
    """
    # Remove trailing whitespace
    hey_bob=hey_bob.strip()

    # Remove spaces b/w words
    hey_bob=hey_bob.replace(" ","")

    # Remove \'
    hey_bob=hey_bob.replace("\'","")

    if hey_bob.isupper() and not hey_bob.endswith('?'):
        return 'Whoa, chill out!'
    elif hey_bob.endswith('?') and not hey_bob.isupper():
        return 'Sure.'
    elif hey_bob.isupper() and hey_bob.endswith('?'):
        return 'Calm down, I know what I\'m doing!'
    elif hey_bob=="" or hey_bob.isspace():
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
