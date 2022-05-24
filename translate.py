import re
from googletrans import Translator

translator = Translator()


def EngToRu(engText:str):
    result = translator.translate(text=engText, dest='ru')
    return result.text

def RuToEng(ruText:str):
    result = translator.translate(text=ruText, dest='en')

    return result.text

