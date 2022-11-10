from googletrans import Translator
translator = Translator()
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translation_words = {w: translator.translate(w, dest="en").text for w in french_words}
print(translation_words)