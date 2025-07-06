import spacy
import json
import sys

def extrair_pessoas(texto):
    nlp = spacy.load("pt_core_news_sm")
    doc = nlp(texto)
    pessoas = set(ent.text for ent in doc.ents if ent.label_ == "PER")
    return {"pessoas": list(pessoas)}

if __name__ == "__main__":
    texto = 'João da Silva foi ao Rio de Janeiro visitar a sede da Petrobras.'
    if len(sys.argv) < 2:
        print("Uso: python extrair_pessoas.py '"+ texto +"'")
        sys.exit(1)
    texto = sys.argv[1]
    resultado = extrair_pessoas(texto)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))