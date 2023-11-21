import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

# Function to calculate similarity between two words
def word_similarity(word1, word2):
    token1 = nlp(word1)
    token2 = nlp(word2)
    
    similarity_score = token1.similarity(token2)
    return similarity_score

# Example usage
# similarity_score = word_similarity("dog", "cat")
# print(similarity_score)

# word_pairs = [
#     ('good', 'intrusive'),
#     ('bad', 'intrusive'),
#     ('good', 'bad')
# ]

# for word1, word2 in word_pairs:
#     print('similarity between', word1, 'and', word2)
#     similarity_score = word_similarity(word1, word2)
#     print(similarity_score)

# Register the custom extension attribute 'synonyms'
spacy.tokens.Token.set_extension('synonyms', default=[])

for word in ['intrusive', 'good', 'bad']:
    print('synonyms of', word)
    synonyms = []
    token = nlp(word)[0]
    
    for syn in token._.synonyms:
        synonyms.append(syn.text)

    print(synonyms)