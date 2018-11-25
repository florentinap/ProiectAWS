from owlready2 import * 
from SPARQLWrapper import SPARQLWrapper, JSON
from googletrans import Translator


def downloadOntology():
	onto_path.append("./resources/ontologies/")

	ontobee = get_ontology("http://purl.obolibrary.org/obo/doid.owl")
	ontobee.load()
	ontobee.save()

def getSynonymColumn(sparql):
	query = """
	SELECT ?uri ?hasExactSynonym {
		?uri <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> ?hasExactSynonym
	}
	"""

	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	synonymResults = []
	for result in results["results"]["bindings"]:
		synonymResults += [result["hasExactSynonym"]["value"]]

	return synonymResults

def translateSynonym(synonym):
	translator = Translator()
	return translator.translate(synonym, dest='ro').text

def insertTranslation(sparql, valueRo, valueEn):
	query = """ 
	INSERT { 
		?uri <http://www.w3.org/2002/07/rdfs#label> "%s"@ro
	} 
	WHERE { 
		?uri <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> "%s"
	} 
	"""%(valueRo, valueEn)
	
	sparql.setQuery(query) 
	sparql.method = 'POST'
	result = sparql.query()

	return result

def getTranslatedLabels(sparql):
	query = """
	SELECT ?uri ?hasExactSynonym ?label {
		?uri <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> ?hasExactSynonym .
  		?uri <http://www.w3.org/2002/07/rdfs#label> ?label 
  		FILTER (langMatches( lang(?label), "ro" )) 
	}
	"""

	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	translatedResults = []
	for result in results["results"]["bindings"]:
		translatedResults += [result["label"]["value"]]

	return translatedResults


def main():
	sparqlQuery = SPARQLWrapper("http://localhost:3030/ds/query")
	sparqlUpdate = SPARQLWrapper("http://localhost:3030/ds/update")

	synonymColumn = getSynonymColumn(sparqlQuery)

	for synonym in synonymColumn:
		translatedSynonym = translateSynonym(synonym)
		insertTranslation(sparqlUpdate, translatedSynonym, synonym)

	print(len(getTranslatedLabels(sparqlQuery)))

main()

