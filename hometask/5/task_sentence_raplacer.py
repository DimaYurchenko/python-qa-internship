# Write a python program that will replace a word with a given length by the provided word
# Example if I have a sentence:
# This is a brown fox
# Add more tests for this as an example below

sentence = "Beginners when start programming often get bored if they do not get a chance to " \
           "play with some interesting code."


def replace_words(text, length_to_replace, word):
    return ' '.join(map(lambda w: word if len(w) == length_to_replace else w, text.split()))


assert replace_words(sentence, 3,
                     "test") == "Beginners when start programming often test bored if they do test test a chance " \
                                "to play with some interesting code."

sentence = "Saepe non et et minus praesentium tenetur recusandae vel esse."

assert replace_words(sentence, 2, "fish") == "Saepe non fish fish minus praesentium tenetur recusandae vel esse."

sentence = "Deserunt ipsam minim repudiandae aut error sint inventore accusantium at."

assert replace_words(sentence, 5, "lorem") == "Deserunt lorem lorem repudiandae aut lorem sint inventore accusantium at."