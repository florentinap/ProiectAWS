from SPARQLWrapper import SPARQLWrapper, JSON


def getSynonymColumn(sparql):
	query = """
	SELECT DISTINCT ?uri ?hasExactSynonym {
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
	SELECT DISTINCT ?uri ?hasExactSynonym ?label {
		?uri <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> ?hasExactSynonym .
  		?uri <http://www.w3.org/2002/07/rdfs#label> ?label 
  		FILTER (langMatches(lang(?label), "ro" )) 
	}
	"""

	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	translatedResults = {}
	for result in results["results"]["bindings"]:
		translatedResults[result["uri"]["value"]] = (result["hasExactSynonym"]["value"], result["label"]["value"])

	return translatedResults

def getAllergy(sparql):
	# query = """
	# SELECT  ?uri ?name ?allergy
	# WHERE {
	# 	?uri <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> ?name .
 #  		?uri <http://www.w3.org/2002/07/owl#annotatedTarget> ?allergy 
 #  		FILTER (contains(?allergy, "has_allergic_trigger"))
	# }
	# """

	query = """
		SELECT ?uri ?allergy {
  			?uri <http://www.w3.org/2000/01/rdf-schema#label> ?allergy 
  			FILTER (contains(?allergy, "allergy"))
		}
	"""

	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	synonymResults = {}
	for result in results["results"]["bindings"]:
		synonymResults[result["uri"]["value"]] = result["allergy"]["value"]
	
	return synonymResults