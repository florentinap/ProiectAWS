from SPARQLWrapper import SPARQLWrapper, JSON


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