from ibm_watson import SpeechToTextV1  # SpeechToText library from ibm.
from ibm_watson import LanguageTranslatorV3
# API Keys. Ein Weg für Zugang zur API.


# Wir erstellen einen Sprach-zu-Text programm mithilfe von der
# IBM speechtotext Cloud API. To Use the API you need a free IBM Cloud Accound.
url_s2t = "https://stream.watsonplatform.net/speech-to-text/api"
iam_apikey_s2t = "thisismyAPIKey"
s2t = SpeechToTextV1(iam_apikey=iam_apikey_s2t, url=url_s2t)  # Dieses Objekt wird für die Kommunikatin mit dem Service verwendet.

filename = "pathtomyWAVfile.wav"
with open(filename, mode="rb") as wav:
    response = s2t.recognize(audio=wav, content_type="audio/wav")  # This sends a get result, the Audiofile to the Cloudservice
    # content_type ist das audioformat.
response.result  # Als Antowort erhalten wir ein Dictionary results

#  Die Antwort:
# {"result":[{"alternatives":[{confidence": 0.91, "transcript": "this will be the translated text"}], "final": True}], "result_index":0}

# Wir benötigen nur den Inhalt des Dictionarys mit dem Key "transcript"
recognized_text = response.result["results"][0]["alternatives"][0]["transcripts"]

# Wir haben nun den Text aus dem WAV file. Dieses können wir nun noch in eine andere Sprache übersetzen

url_lt = "https://gateway.watsonplatform.net/language-translator/api"
apikey_lt = "myAPIKey"
version_lt = "2018-05-01"

language_translator = LanguageTranslatorV3(iam_apikey=apikey_lt, url=url_lt, version=version_lt)  # kreeirt das Objekt
# language_translator.list_identifiable_languages().get_result()  # Zeigt alle verfügbaren Sprachen an etwa so:
# {"languages":[{"language":"af", "name":"Afrikaas"}, ......]}

translation_response = language_translator.translate(text=recognized_text, model_id="en-es")  # übersetzt gesprochene ins spanische
translation = translation_response.get_result()
#  {"translation":[{"translation":"der übersetzte text"{],
#  "word_count":4, "character_count":21}
# wir nehmen uns nur den Text
spanisch_translation = translation["translation"][0]["translation"]
print(spanisch_translation)





