# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text):
    """
    Skriv beskrivning här.
    """
    words = []
    words = text.split(" ")
    numberOfWords = len(words)
    return numberOfWords

sentence = "Hejsan hoppsan igen ok"
wordCount = word_count(sentence)
print(wordCount)