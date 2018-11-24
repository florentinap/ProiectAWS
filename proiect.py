from owlready2 import * 

def downloadOntology():
	onto_path.append("./resources/ontologies/")

	ontobee = get_ontology("http://purl.obolibrary.org/obo/doid.owl")
	ontobee.load()
	ontobee.save()
