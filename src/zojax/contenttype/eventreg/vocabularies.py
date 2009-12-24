from zope.schema.vocabulary import SimpleVocabulary

from config import items_vocabularies, values_vocabularies

vocabularies = dict()

for key, value in values_vocabularies.items():
    vocabularies[key] = SimpleVocabulary.fromValues(value)

for key, value in items_vocabularies.items():
    vocabularies[key] = SimpleVocabulary.fromItems(value)
