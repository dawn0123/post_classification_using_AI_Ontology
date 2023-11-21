import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from nltk.corpus import wordnet

# for word in ['bad', 'good', 'intrusive']:
#     print(f'---------------results for {word}---------------')
#     synsets  = wordnet.synsets(word)
#     print(synsets)
#     for synset in synsets:
#         # synset = synsets[0]  # Select the first synset
#         print(synset)
#         definition = synset.definition()
#         print('definition:', definition)
#         synonyms = synset.lemmas()  # Get synonyms as lemmas
#         synonyms = [lemma.name() for lemma in synonyms]  # Extract lemma names
#         print('synonyms:', synonyms)
#         antonyms = synset.lemmas()[0].antonyms()  # Get antonyms as lemmas
#         antonyms = [lemma.name() for lemma in antonyms]  # Extract lemma names
#         print('antonyms:', antonyms)
#         hypernyms = synset.hypernyms()
#         hyponyms = synset.hyponyms()
#         print('hyponyms:', hyponyms)

# def similarity(word1, word2):
#     word1_synsets = wordnet.synsets(word1)
#     word2_synsets = wordnet.synsets(word2)
#     max_similarity = 0
#     for synset1 in word1_synsets:
#         for synset2 in word2_synsets:
#             similarity = synset1.path_similarity(synset2)
#             if similarity is not None and similarity > max_similarity:
#                 max_similarity = similarity
#     return max_similarity

# ret1 = similarity('good', 'intrusive')
# print('similarity between good and intrusive:', ret1)
# ret2 = similarity('bad', 'intrusive')
# print('similarity between bad and intrusive:', ret2)

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            sword = lemma.name()
            if sword not in synonyms:
                synonyms.append(sword)
    return synonyms

def get_similar_terms(term):
    words = term.split()
    n_words = len(words)
    ret = []
    similar_term = [''] * n_words
    synonyms = [get_synonyms(word) for word in words]
    def make_similar_term(i_word):
        if i_word == n_words:
            ret.append(' '.join(similar_term))
            return
        for syn in synonyms[i_word]:
            similar_term[i_word] = syn
            make_similar_term(i_word + 1)
    
    make_similar_term(0)
    return ret

terms = get_similar_terms('good thoughts')
print(','.join(terms))