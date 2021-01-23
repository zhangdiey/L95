import stanza, spacy

# To install English parsers for stanza
# (python) stanza.download('en')
# To install English parsers for spacy
# python -m spacy download en_core_web_sm

nlp_stanza = stanza.Pipeline('en')
nlp_spacy = spacy.load("en_core_web_sm")

with open('data.txt', 'r') as file:
    sents = file.readlines()
    for index, sent in enumerate(sents):
        sent = sent.strip()
        doc_stanza = nlp_stanza(sent)
        doc_spacy = nlp_spacy(sent)
        print(index+1, ': ', sent, sep='')
        print('stanza:')
        print(*[f'word: {word.text}\tupos: {word.upos}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc_stanza.sentences for word in sent.words], sep='\n')
        print('\nspacy:')
        print(*[f'word: {word.text}\tupos: {word.pos_}\thead: {word.head.text}\tdeprel: {word.dep_}' for word in doc_spacy], sep='\n')
        print('\nEnd of sentence', index+1, '\n')
    print('\nEnd of all test data.')