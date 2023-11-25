import deepl

class DeepLTranslator(Translator):
    def __init__(self, auth_key):
        self.translator = deepl.Translator(auth_key)

    def translate(self, text, target_language='ZH'):
        result = self.translator.translate_text(text, target_lang=target_language)
        return result.text
