from SPARQLWrapper import SPARQLWrapper, JSON
from googletrans import Translator
from updateOntology import *
from queryOntology import *
from translate import *


def main():
	f = open('./resources/synonyms.txt', 'a+')
	sparqlQuery = SPARQLWrapper("http://localhost:3030/doid/query")
	sparqlUpdate = SPARQLWrapper("http://localhost:3030/doid/update")

	synonymColumn = getSynonymColumn(sparqlQuery)
	print(len(synonymColumn))
	content = f.readlines()
	content = [x.strip() for x in content]

	for synonym in synonymColumn:
		if synonym not in content:
			try:
				translatedSynonym = translateSynonym(synonym)
				insertTranslation(sparqlUpdate, translatedSynonym, synonym)
				f.write(synonym + '\n')
			except Exception as e:
				print (e)
				break

	print(len(getTranslatedLabels(sparqlQuery)))
	f.close()

main()
