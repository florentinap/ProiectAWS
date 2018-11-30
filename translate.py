from googletrans import Translator


def translateSynonym(synonym):
	translator = Translator()
	return translator.translate(synonym, dest='ro').text