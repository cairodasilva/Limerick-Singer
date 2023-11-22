import nltk
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

def conjugate_verb(verb, person, tense):
    lemmatizer = WordNetLemmatizer()
    pos_verb = pos_tag([verb])[0][1][0].lower()

    if pos_verb == 'v':
        if tense == 'present':
            if person == 1:
                return lemmatizer.lemmatize(verb, 'v')
            elif person == 2:
                return lemmatizer.lemmatize(verb, 'v') + 's'
            elif person == 3:
                return lemmatizer.lemmatize(verb, 'v') + 's'

# Example usage
verb = "run"
person = 3  # 1 for first person, 2 for second person, 3 for third person
tense = "present"
conjugated_verb = conjugate_verb(verb, person, tense)
print(conjugated_verb)
